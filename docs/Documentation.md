# Documentation
This document provides a detailed explanation of the project.

## File Overviews
1. ```chroma_db/```: this folder acts as a vector database.
2. ```data/```: this folder will contain all the pdf documents.
3. ```question.py```: this file has the q&a program with the LLM.
4. ```setup.py```: this file is the preparation file to index and embed the documents.

## ```setup.py```
```
documents = []
    for filename in os.listdir(data_path):
        if filename.endswith(".pdf"):
            pdf_path =os.path.join(data_path, filename)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
```
This part of code is the indexing part, by making a list for the documents, then list all the available pdfs in the folder and load the pdfs with ```PyPDFLoader``` and extending the documents list by appending elements from the iterable (loader).

```
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)
```
This part of code splits the document contents into chunks with the size of 500 and overlapping by 100.

```
vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model=embed_model),
        persist_directory=chroma_path
    )
```
This part of code creates the embedding using the embed model and stores them into the Chroma DB.

## ```question.py```
```
template = """
    Answer only based on this context: {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
```
This part of code acts as a prompt template to then be used by the LLM.
```
vector_store = Chroma(
        persist_directory=chroma_path,
        embedding_function=OllamaEmbeddings(model=embed_model)
    )
    retriever = vector_store.as_retriever(k=3)

    llm = OllamaLLM(model=llm_model)
```
This part of code loads the DB from ```setup.py``` and set the retriever. The ```k=3``` means top 3 most relevant results. Also create the LLM model.
```
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```
This part of code is to set the chain process in RAG. It first finds related info from the database with the ```retriever```. Then it combines the user question with the prompt. After combined, it asks the LLM using the information. Lastly, gets clean text output for display.
```
while True:
    query = input("> ")
    if query == "exit":
        print("Thank you!")
        break

    response = chain.invoke(query)
    print("\n------------")
    print(response)
    print("\n------------\n")
```
This part of code is the main part of Q&A. The program will always loop the query, if the query is ```exit```, it will stop the program. If not, the query will be sent to the chain. And lastly prints the output.