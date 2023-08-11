import os

import gradio as gr
from dotenv import load_dotenv

from KoPrivateGPT.options import Options
from KoPrivateGPT.pipeline import BasicIngestPipeline
from KoPrivateGPT.utils.embed import Embedding
from KoPrivateGPT.utils.model import load_model
from KoPrivateGPT.retrieval import VectorDBRetrieval
from KoPrivateGPT.utils.util import slice_stop_words

load_dotenv()

STOP_WORDS = ["#", "답변:", "응답:", "맥락:", "?"]

DEVICE = "mps"
MODEL_TYPE = "OpenAI"
llm = load_model(MODEL_TYPE)
EMBEDDING_TYPE = "OpenAI"
DB_TYPE = "chroma"
embeddings = Embedding(embed_type=EMBEDDING_TYPE, device_type=DEVICE)

GRADIO_DB_PATH = os.path.join(Options.root_dir, )


def ingest(files) -> str:
    # TODO : add file cache for gradio version
    file_paths = [f.name for f in files]
    ingest_pipeline = BasicIngestPipeline(file_loader_type=("file_loader", {"target_dir": file_paths}),
                                          retrieval_type=("vector_db", {"vectordb_type": DB_TYPE,
                                                                        "embedding": embeddings}))
    ingest_pipeline.run()
    return "Ingest Done"


def make_answer(text):
    chain = make_llm_chain(llm)
    # Get the answer from the chain
    answer, docs = get_answer(chain, retriever, text)
    answer = slice_stop_words(answer, STOP_WORDS)
    document_source = ",\n".join([doc.metadata["source"].split("/")[-1] for doc in docs])
    return answer, document_source


with gr.Blocks(analytics_enabled=False) as demo:
    gr.HTML(
        f"""<div style="text-align: center; max-width: 500px; margin: 0 auto;">
                <div>
                <h1>KoPrivateGPT with {MODEL_TYPE}</h1>
                </div>
                <div>
                Demo runs on {DEVICE}
                </div>
            </div>"""
    )
    with gr.Row():
        with gr.Column(scale=2):
            query = gr.Textbox(label="질문 내용", placeholder="질문을 입력하세요", interactive=True, lines=17, max_lines=17)
            question_btn = gr.Button("질문하기")

        with gr.Column(scale=3):
            answer_result = gr.Textbox(label="답변 내용", placeholder="답변을 출력합니다.", interactive=False, lines=20,
                                       max_lines=20)

    gr.HTML(
        """<h2 style="text-align: center;"><br>파일 업로드하기<br></h2>"""
    )
    upload_files = gr.Files()
    ingest_status = gr.Textbox(value="", label="Ingest Status")
    ingest_button = gr.Button("Ingest")
    ingest_button.click(ingest, inputs=[upload_files], outputs=[ingest_status])

    document_sources = gr.Textbox(label="참조한 문서", placeholder="참조한 문서를 출력합니다.", interactive=False)
    question_btn.click(make_answer, inputs=[query], outputs=[answer_result, document_sources])

demo.launch(share=False, debug=True, server_name="0.0.0.0")
