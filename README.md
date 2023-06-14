# 중요!
해당 레포는 아직 개발 중입니다!

# KoPrivateGPT

본 프로젝트는 [privateGPT](https://github.com/imartinez/privateGPT)와 [localGPT](https://github.com/PromtEngineer/localGPT)에서 영감을 받아 만들어졌습니다. 

해당 프로젝트들은 여러 문서들을 벡터 DB에 저장을 하여, 문서 내용에 대해 LLM과 대화할 수 있는 프로젝트입니다. 오픈소스 Document Q&A라고 보시면 됩니다.

그러나 해당 프로젝트들은 한국에서 활용하기 어려울 정도의 성능을 한국어에서 보여줍니다. 이를 해결하기 위하여 한국어 버전의 KoPrivateGPT 프로젝트를 만들었습니다.

한국어를 이용하여 오프라인에서도 모든 문서들에 대해 LLM에게 질문을 해보세요. 100% 프라이버시가 보장되며, 어떠한 데이터도 외부로 전송되지 않습니다. 인터넷 연결 없이 문서를 불러오고 질문을 해보세요!

원래 프로젝트에서 한국에 맞게 변형한 부분은 현재까지 다음과 같습니다. 
- 한국어 모델 [KoAlpaca](https://github.com/Beomi/KoAlpaca) 적용
- 한국어 임베딩 [Korean-Sentence-Embedding](https://github.com/BM-K/Sentence-Embedding-Is-All-You-Need) 적용
- HWP 파일 문서 호환 추가 ([hwp-converter-api](https://github.com/edai-club/hwp-converter-api) 사용)

## Colab 데모
콜랩에서 실행할 수 있는 데모 버전을 준비하였습니다. 아쉽게도 콜랩 버전에서 HWP 파일은 사용할 수 없습니다. 
[여기](https://colab.research.google.com/drive/1wFV8WSfna0p1HYD_N8KmlrB69ItWczsZ?usp=sharing)에서 콜랩 데모 버전을 실행해보세요.
<a style='display:inline' target="_blank" href="https://colab.research.google.com/drive/1wFV8WSfna0p1HYD_N8KmlrB69ItWczsZ?usp=sharing">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

# 환경 설정
해당 프로젝트를 실행하기 위해서 아래의 코드를 실행해주세요. 파이썬 3.10 이상이 설치된 환경에서의 실행을 추천합니다.

```shell
git clone https://github.com/edai-club/KoPrivateGPT.git
cd KoPrivateGPT
pip install -r requirements.txt
```

## 테스트 데이터
해당 레포에서는 [제주 제2항 기본계획(안) 보도자료](https://www.korea.kr/common/download.do?fileId=197236015&tblKey=GMN)를 예시로 사용합니다.

# 직접 원하는 문서를 불러오는 법
SOURCE_DOCUMENTS 폴더 안에 원하는 .txt, .pdf, .csv, .hwp, 혹은 .xlsx 파일을 넣어주세요.

현재는 .txt, .pdf, .csv, .xlsx, .hwp 파일만 지원합니다. 다른 파일을 사용하고 싶으시면, 해당 파일을 지원하는 파일로 변환을 해야 합니다.

그리고 아래 코드를 이용하여 모든 문서를 불러옵니다. 
    
 ```shell  
python ingest.py
 ```
위 코드를 실행하면 문서들을 텍스트 뭉치로 자른 뒤, 한국어 임베딩을 사용하여 벡터로 임베딩하고 그것을 chroma 벡터 DB로 저장합니다. 
저장은 DB 폴더에 되며, 만약 모든 데이터를 삭제하고 싶다면 DB 폴더를 완전히 삭제하면 됩니다.

# LLM에게 질문하는 법
질문을 하기 위해서는 다음과 같이 실행하면 됩니다.

```shell
python run_localGPT.py
```
이후 아래 명령어가 나오면, 원하는 질문을 입력하면 됩니다. 
```shell
> 질문:
```

위 코드를 실행하면 문서들을 텍스트 뭉치로 자른 뒤, 한국어 임베딩을 사용하여 벡터로 임베딩하고 그것을 chroma 벡터 DB로 저장합니다. 저장은 DB 폴더에 되며, 만약 모든 데이터를 삭제하고 싶다면 DB 폴더를 완전히 삭제하면 됩니다. '
조금 기다리면 인공지능의 답변이 제공되며, 해당 답변을 제공하는데에 참조한 문서 4개의 출처와 그 내용이 출력됩니다. 

'exit' 혹은 '종료' 를 입력하면 실행이 종료됩니다.

## OpenAI 모델 사용법
기기의 성능이 부족해 KoAlpaca 구동에 실패하였다면, OpenAI 모델을 사용하세요.
데이터가 OpenAI에 제공되어 완전히 private 하지는 않지만, 낮은 성능의 기기에서도 실행할 수 있습니다. 

아래의 코드에 본인의 OpenAI 토큰을 넣어 구동할 수 있습니다.
```shell
python run_localGPT.py --model_type=openai --openai-token=<Your OPENAI TOKEN>
```

# 질문 및 답변 예시 - KoAlpaca Polyglot
```markdown
- 
```


# 시스템 요구 사항

## 파이썬 버전
이 소프트웨어를 사용하려면 Python 3.10 이상이 설치되어 있어야 합니다. 이전 버전의 Python은 컴파일되지 않을 수 있습니다.

## C++ 컴파일러
'pip install'을 하는 중에 오류가 발생하면 컴퓨터에 C++ 컴파일러를 설치해야 할 수 있습니다.

### Windows 10/11의 경우
Windows 10/11에서 C++ 컴파일러를 설치하려면 다음 단계를 따르세요:

1. Visual Studio 2022를 설치합니다.
2. 다음 컴포넌트가 선택되어 있는지 확인합니다:
   * 범용 Windows 플랫폼 개발
   * Windows용 C++ CMake 툴
3. MinGW 홈페이지](https://sourceforge.net/projects/mingw/)에서 MinGW 설치 파일을 다운로드합니다.
4. 설치 파일을 실행하고 "gcc" 컴포넌트를 선택합니다.

### NVIDIA 드라이버 문제:
이 [페이지](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-22-04)를 참고하여 NVIDIA 드라이버를 설치합니다.
        

# 면책 조항
이 프로젝트는 LLM 및 벡터 임베딩을 사용하여 한국어로 질문에 답변할 수 있는 완전한 로컬 솔루션의 가능성을 검증하기 위한 시험용 프로젝트입니다. 
프로덕션 활용을 위한 준비는 완료되지 않았으며 프로덕션에 사용할 수 없습니다.


# KoPrivateGPT

This project was inspired by the original [privateGPT](https://github.com/imartinez/privateGPT) and [localGPT](https://github.com/PromtEngineer/localGPT). Most of the description here is inspired by the original privateGPT and original localGPT.

In this model, I have replaced the GPT4ALL model with KoAlpaca-Polyglot model, and we are using the Korean Sentence Embeddings instead of LlamaEmbeddings as used in the original privateGPT.

Plus, we add HWP converter for ingesting HWP files that crucial to Korean businessmen and women.

Ask questions to your documents without an internet connection, using the power of LLMs. 100% private, no data leaves your execution environment at any point. You can ingest documents and ask questions without an internet connection!

Built with [LangChain](https://github.com/hwchase17/langchain) and [KoAlpaca](https://github.com/Beomi/KoAlpaca) and [Korean-Sentence-Embedding](https://github.com/BM-K/Sentence-Embedding-Is-All-You-Need)


# Environment Setup
In order to set your environment up to run the code here, first install all requirements:

```shell
git clone https://github.com/edai-club/KoPrivateGPT.git
cd KoPrivateGPT
pip install -r requirements.txt
```

## Test dataset
This repo uses a [대한민국 상법](https://constitutioncenter.org/media/files/constitution.pdf) as an example.

## Instructions for ingesting your own dataset

Put any and all of your .txt, .pdf, .csv or .hwp files into the SOURCE_DOCUMENTS directory
in the load_documents() function, replace the docs_path with the absolute path of your source_documents directory. 

The current default file types are .txt, .pdf, .csv, .xlsx, .hwp, if you want to use any other file type, you will need to convert it to one of the default file types.


Run the following command to ingest all the data.

```shell
python ingest.py
```

It will create an index containing the local vectorstore. Will take time, depending on the size of your documents.
You can ingest as many documents as you want, and all will be accumulated in the local embeddings database. 
If you want to start from an empty database, delete the `index`.

Note: When you run this for the first time, it will download take time as it has to download the embedding model. In the subseqeunt runs, no data will leave your local enviroment and can be run without internet connection.


## Ask questions to your documents, locally!
In order to ask a question, run a command like:

```shell
python run_localGPT.py
```

And wait for the script to require your input. 

```shell
> Enter a query:
```

Hit enter. Wait while the LLM model consumes the prompt and prepares the answer. Once done, it will print the answer and the 4 sources it used as context from your documents; you can then ask another question without re-running the script, just wait for the prompt again. 

Note: When you run this for the first time, it will need internet connection to download the KoAlpaca model. After that you can turn off your internet connection, and the script inference would still work. No data gets out of your local environment.

Type `exit` to finish the script.

# Run it on OpenAI
By default, this project use KoAlpaca-Polyglot model for private use. 
For Ingestion run the following: 
```shell
python ingest.py --device_type cpu
```
In order to ask a question, run a command like:

```shell
python run_localGPT.py --device_type cpu
```

# System Requirements

## Python Version
To use this software, you must have Python 3.10 or later installed. Earlier versions of Python will not compile.

## C++ Compiler
If you encounter an error while building a wheel during the `pip install` process, you may need to install a C++ compiler on your computer.

### For Windows 10/11
To install a C++ compiler on Windows 10/11, follow these steps:

1. Install Visual Studio 2022.
2. Make sure the following components are selected:
   * Universal Windows Platform development
   * C++ CMake tools for Windows
3. Download the MinGW installer from the [MinGW website](https://sourceforge.net/projects/mingw/).
4. Run the installer and select the "gcc" component.

### NVIDIA Driver's Issues:
Follow this [page](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-22-04) to install NVIDIA Drivers.
        

# Disclaimer
This is a test project to validate the feasibility of a fully local solution for question answering using LLMs and Vector embeddings. It is not production ready, and it is not meant to be used in production. Vicuna-7B is based on the Llama model so that has the original Llama license. 
