from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

setup(
    name='KoPrivateGPT',
    version='0.1',
    packages=find_packages(where='.'),
    package_dir={'': '.'},
    url="https://github.com/NomaDamas/KoPrivateGPT",
    license='Apache License 2.0',
    py_modules=[splitext(basename(path))[0] for path in glob('./*.py')],
    install_requires=[
        'langchain==0.0.309',
        'chromadb==0.4.5',
        'urllib3',
        'pdfminer.six',
        'click',
        'openpyxl',
        'pinecone-client',
        'python-dotenv==1.0.0',
        'tiktoken',
        'rank_bm25',
        'numpy',
        'pandas',
        'pydantic',
        'tqdm',
        'pymongo',
        'requests',
        'redis',
        'aiohttp',
        'openai',
        'InstructorEmbedding',
        'sentence-transformers',
        'huggingface_hub',
        'transformers',
        'torch',
        'pyarrow',
        'fastparquet'
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: Apache License 2.0',
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
