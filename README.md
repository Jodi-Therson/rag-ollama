# RAG with Ollama
A simple Retrieval-Augmented Generation (RAG) implementation with Ollama LLM.
This project demonstrates how to connect an LLM from Ollama with an external document store to answer questions based on your own data.

## Project Structure
```
rag-ollama/
├── chroma_db           # Auto-generated after running setup.py
├── data                # Folder for your datas
│  └── yourpdf.pdf      # Example PDF
├── question.py         # The Q & A Program based on the document provided
└── setup.py            # Setting up the Documents
```

## Prerequisites
- [Ollama](https://ollama.com)
- An [LLM model](https://ollama.com/search) and an embedding model installed in Ollama
- [Python 3.13 +](https://python.org)
- [Git](https://git-scm.com/downloads)

## Configuration
This project uses an Ollama LLM model.
By default, the embedding model is set to 'mxbai-embed-large' and the LLM model is set to 'mistral'.
You can change it to any model you have installed in Ollama.

**To change the model:**
1. Open ```setup.py```
2. Look for this ``embed_model = "mxbai-embed-large"``
3. Change ```"mxbai-embed-large"``` with the name of your desired model.
4. Same goes for ```question.py```
5. Look for ```llm_model = "mistral"```
6. Change ```"mistral"``` with the name of your desired model.

## Steps:
1. Clone the repository:
```
git clone https://github.com/Jodi-Therson/rag-ollama.git
cd rag-ollama
```
### Extra Steps before installing the dependencies
- Use Virtual Environment:
```
python -m venv .venv
.venv\Scripts\activate
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Create a folder named ```data/``` and place your PDF files inside the ```data/``` folder.
4. Run setup.py first, then run question.py.
```
python setup.py
python question.py
```

For detailed explanation, see: [Documentation](docs/Documentation.md)