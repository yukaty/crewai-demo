from pathlib import Path

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

load_dotenv()

INDEX_DIR = Path("data/faiss_index")
DOCS_PATH = Path("docs/sample.txt")


def build_or_load_vectorstore(force_reindex=False):
    # Initialize embeddings
    embeddings = OpenAIEmbeddings()

    # Load existing index if available
    if INDEX_DIR.exists() and not force_reindex:
        return FAISS.load_local(
            INDEX_DIR, embeddings, allow_dangerous_deserialization=True
        )

    # Load document
    text = DOCS_PATH.read_text(encoding="utf-8")

    # Chunk documents by line breaks
    chunks = [line.strip() for line in text.splitlines() if line.strip()]

    # Create FAISS vector store
    vectorstore = FAISS.from_texts(chunks, embeddings)

    # Save the vector store locally
    vectorstore.save_local(INDEX_DIR)

    return vectorstore
