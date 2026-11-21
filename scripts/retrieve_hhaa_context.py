import sys
import sqlite3
from llama_index import VectorStoreIndex
from chromadb import Client

def get_hhaa_context(topic):
    # Query literature_kb.db
    lit_conn = sqlite3.connect('/root/emi_knowledge/literature_kb.db')
    lit_results = lit_conn.execute(f"SELECT * FROM chunks WHERE content LIKE '%{topic}%' LIMIT 5").fetchall()
    
    # Query HHAA's Chroma vector store
    chroma_client = Client()
    chroma_collection = chroma_client.get_collection(name="henry_hub_pit")
    chroma_results = chroma_collection.query(query_texts=[topic], n_results=3)
    
    # Query HHAA's SQLite databases
    hh_conn = sqlite3.connect('/root/henry_hub_atomic_agents/henry_hub_pit.db')
    hh_results = hh_conn.execute(f"SELECT * FROM market_facts WHERE topic LIKE '%{topic}%' LIMIT 5").fetchall()
    
    return {
        'literature': lit_results,
        'chroma': chroma_results,
        'sqlite': hh_results
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 retrieve_hhaa_context.py <topic>")
        sys.exit(1)

    context = get_hhaa_context(sys.argv[1])
    print(f"Literature results for {sys.argv[1]}:")
    for row in context['literature']:
        print(f"- {row[0]}...")

    print(f"\nChroma results for {sys.argv[1]}:")
    for doc in context['chroma']['documents'][0]:
        print(f"- {doc[:200]}...")

    print(f"\nSQLite results for {sys.argv[1]}:")
    for row in context['sqlite']:
        print(f"- {row[0]}...")