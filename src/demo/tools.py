from typing import Dict, List

from crewai.tools import tool
from demo.vectorstore import build_or_load_vectorstore


def _retrieve_docs(query: str, k: int = 3) -> List[Dict]:
    try:
        vectorstore = build_or_load_vectorstore()
        retriever = vectorstore.as_retriever(search_kwargs={"k": k})

        docs = retriever.invoke(query)

        results = []
        for i, doc in enumerate(docs, start=1):
            results.append(
                {"rank": i, "content": doc.page_content, "metadata": doc.metadata or {}}
            )
        return results
    except Exception as e:
        print(f"❌ Error occurred: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()
        return []


@tool("search_internal_documents")
def search_internal_documents(query: str) -> str:
    """
    Search internal documents (local FAISS) and return results.
    Args:
        query: Search query
    Returns:
        Search results as a formatted string
    """
    results = _retrieve_docs(query, k=3)

    if not results:
        return "Search results: No documents found."

    # Format results for agent readability
    lines = ["【Internal Document Search Results】"]
    for r in results:
        title = r["metadata"].get("source", "internal")
        lines.append(f"\n---\n[{r['rank']}] +source={title}\n{r['content']}")

    output = "\n".join(lines)
    return output
