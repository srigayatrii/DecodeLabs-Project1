from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="db",
    embedding_function=embedding
)

queries = {
    "Risks": "What risks or liabilities are mentioned?",
    "Dates": "What important dates or durations are mentioned?",
    "Stakeholders": "Who are the parties involved in this agreement?"
}

for category, query in queries.items():

    print(f"\n========== {category.upper()} ==========\n")

    results = vectorstore.similarity_search(query, k=2)

    for i, result in enumerate(results):

        print(f"\n--- Source {i+1} ---")
        print("Page:", result.metadata.get("page"))
        print(result.page_content[:500])