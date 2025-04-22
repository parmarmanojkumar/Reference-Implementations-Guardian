# rag_cli.py
# Usage:
#   export OPENAI_API_KEY="your_openai_key"
#   export GUARDIAN_API_KEY="your_guardian_key"
#   export GUARDIAN_BASE_URL="https://your.guardian.api"
#   python3 rag_cli.py index <path_to_file>
#   python3 rag_cli.py query "Your question?"

import os
import sys
import argparse
from termcolor import colored
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Import Guardian API classes
from guardian_api import GuardianAPIConfig, CheckResult

# Constants
INDEX_DIR = "faiss_index"
EMBED_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Initialize embeddings
embeddings = SentenceTransformerEmbeddings(model_name=EMBED_MODEL)

# Initialize Guardian API
def init_guardian():
    api_key = os.getenv("GUARDIAN_API_KEY")
    base_url = os.getenv("GUARDIAN_BASE_URL")
    if not api_key or not base_url:
        print(colored("GUARDIAN_API_KEY and GUARDIAN_BASE_URL must be set.", "red"))
        sys.exit(1)
    try:
        cfg = GuardianAPIConfig(api_key=api_key, base_url=base_url)
        return cfg
    except Exception as e:
        print(colored(f"Failed to initialize Guardian API: {e}", "red"))
        sys.exit(1)


def index_file(file_path: str):
    """
    Load a file, split into chunks, run guardrail checks, and index approved chunks.
    """
    if not os.path.exists(file_path):
        print(colored(f"File not found: {file_path}", "red"))
        sys.exit(1)

    guardian = init_guardian()

    # Load documents
    if file_path.lower().endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path, encoding="utf-8")
    docs = loader.load()

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(docs)
    print(colored(f"Total chunks created: {len(chunks)}", "cyan"))

    # Filter chunks via Guardian API
    approved = []
    for i, chunk in enumerate(chunks, 1):
        text = chunk.page_content if hasattr(chunk, 'page_content') else chunk.content
        result = guardian.check_input(text)
        if result.approved:
            approved.append(chunk)
        else:
            print(colored(f"Chunk {i} blocked: {result.message}", "yellow"))
    print(colored(f"Approved chunks: {len(approved)}", "green"))

    # Create or update FAISS index
    if os.path.exists(INDEX_DIR):
        db = FAISS.load_local(INDEX_DIR, embeddings)
        db.add_documents(approved)
        print(colored(f"Added {len(approved)} chunks to existing index.", "green"))
    else:
        db = FAISS.from_documents(approved, embeddings)
        db.save_local(INDEX_DIR)
        print(colored(f"Created new index with {len(approved)} chunks.", "green"))


def query_loop(question: str):
    """
    Query the existing FAISS index and print an answer.
    """
    if not os.path.exists(INDEX_DIR):
        print(colored("No index found. Please run 'index' first.", "red"))
        sys.exit(1)

    db = FAISS.load_local(INDEX_DIR, embeddings)
    retriever = db.as_retriever()
    llm = OpenAI()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    answer = qa.run(question)
    print("\n--- Answer ---")
    print(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple RAG CLI with Guardian guardrails")
    subparsers = parser.add_subparsers(dest="command")

    # index subcommand
    idx = subparsers.add_parser("index", help="Index a PDF or text file with guardrails")
    idx.add_argument("path", help="Path to .pdf or .txt file to index")

    # query subcommand
    qry = subparsers.add_parser("query", help="Ask a question against indexed docs")
    qry.add_argument("question", help="Your query string, e.g. 'What is...' ")

    args = parser.parse_args()

    if args.command == "index":
        index_file(args.path)
    elif args.command == "query":
        query_loop(args.question)
    else:
        parser.print_help()
 