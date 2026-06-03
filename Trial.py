import marimo

__generated_with = "0.23.8"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import os
    from os import path
    from dotenv import load_dotenv

    return (os,)


@app.cell
def _():
    from langchain_community.document_loaders import TextLoader
    from langchain_community.document_loaders import DirectoryLoader

    return DirectoryLoader, TextLoader


@app.cell
def _():
    docs_path = "C:\\Users\\ASUS\\Omnisearch-RAG\\data"
    return (docs_path,)


@app.cell
def _(DirectoryLoader, TextLoader, os):
    def load_documents(docs_path="data"):
        #Load all documents from the specified directory.
        print(f"Loading documents from {docs_path}...")

        #check if docs directory exists
        if not os.path.exists(docs_path):
            raise FileNotFoundError(f"The directory {docs_path} does not exist. Please create it and add your company files.")

        #Load all .txt files from the docs directory
        loader = DirectoryLoader(
            path=docs_path,
            glob="*.txt",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            show_progress=True
        )
        #Loading all text files into documents variable
        documents = loader.load()

        #Raise an error if no documents were found in the directory
        if len(documents) == 0:
            raise FileNotFoundError(f"No .txt files found in the {docs_path} directory. Please add some text files to ingest.")

        #Print out some information about the loaded documents for verification
        for i, doc in enumerate(documents[:2]):
            print(f"\nDocument {i+1}:")
            print(f"    Source: {doc.metadata['source']}")
            print(f"    Content length: {len(doc.page_content)} characters")
            print(f"    Content preview: {doc.page_content[:100]}...")
            print(f"    Metadata: {doc.metadata}")

        #return the loaded documents for further processing, chunking or storing as raw in database
        return documents

    return (load_documents,)


@app.cell
def _(docs_path, load_documents):
    documents = load_documents(docs_path)
    return (documents,)


@app.cell(column=1)
def _():
    from langchain_text_splitters import CharacterTextSplitter

    return (CharacterTextSplitter,)


@app.cell
def _(CharacterTextSplitter):
    def split_documents(documents, chunk_size=1000, chunk_overlap=0):
        """Split documents into smaller chunks with overlap"""
        print("Splitting documents into chunks...")

        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap
        )

        chunks = text_splitter.split_documents(documents)

        if chunks:

            for i, chunk in enumerate(chunks[:5]):
                print(f"\n--- Chunk {i+1} ---")
                print(f"Source: {chunk.metadata['source']}")
                print(f"Length: {len(chunk.page_content)} characters")
                print(f"Content:")
                print(chunk.page_content)
                print("-" * 50)

            if len(chunks) > 5:
                print(f"\n... and {len(chunks) - 5} more chunks")

        return chunks

    return (split_documents,)


@app.cell
def _(documents, split_documents):
    chunks = split_documents(documents)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
