import os
from dotenv import load_dotenv

#from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
#from langchain_docling import DoclingLoader

load_dotenv()

"""--------LANGCHAIN DOCLING DOCUMENT LOADER--------"""
"""def load_documents(docs_path="data"):
    
    all_documents = []
    supported_extensions = ["*.pdf", "*.docx", "*.pptx"]
    
    print(f"Loading documents from {docs_path} using DoclingLoader...")
    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"The directory {docs_path} does not exist. Please create it and add your company files.")
    
    for ext in supported_extensions:
        for file_path in directory_path.glob(ext):
            print(f"Loading {file_path.name}...")
            try:
                loader = DoclingLoader(
                    file_path=str(file_path),
                    export_type=ExportType.MARKDOWN,
                    show_progress=True
                )
            except Exception as e:
                print(f"Error loading {file_path.name}: {e}")
    

    if len(documents) == 0:
        raise FileNotFoundError(f"No .txt files found in the {docs_path} directory. Please add some text files to ingest.")
    for i, doc in enumerate(documents[:2]):
        print(f"\nDocument {i+1}:")
        print(f"    Source: {doc.metadata['source']}")
        print(f"    Content length: {len(doc.page_content)} characters")
        print(f"    Content preview: {doc.page_content[:100]}...")
        print(f"    Metadata: {doc.metadata}")
        
    return documents
"""


"""--------LANGCHAIN-COMMUNITY DOCUMENT LOADER--------"""
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
             
              
def main():
    """MAIN INGESTION PIPELINE"""
    print("===RAG Document Ingestion Pipeline===")
    
    #define paths
    docs_path = "C:\\Users\\ASUS\\Omnisearch-RAG\\data"
    
    #Step 1: Load documents from the specified directory
    documents = load_documents(docs_path)
    print("Ingestion process completed successfully.")
    print(len(documents), "documents loaded and ready for processing.")
    #persistent_directory = "db/chroma_db"
    
    
if __name__ == "__main__":
    main()