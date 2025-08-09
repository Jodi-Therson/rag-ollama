from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

chroma_path = "chroma_db"
llm_model = "mistral"
embed_model = "mxbai-embed-large"

def main():
    # Create a prompt template
    template = """
    Answer only based on this context: {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # Load the chroma and set up the retriever
    vector_store = Chroma(
        persist_directory=chroma_path,
        embedding_function=OllamaEmbeddings(model=embed_model)
    )
    retriever = vector_store.as_retriever(k=3)

    llm = OllamaLLM(model=llm_model)

    # Create RAG chain
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # The program
    while True:
        query = input("> ")
        if query == "exit":
            print("Thank you!")
            break

        response = chain.invoke(query)
        print("\n------------")
        print(response)
        print("\n------------\n")

if __name__ == "__main__":
    main()