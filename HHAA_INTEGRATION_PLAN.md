# Henry Hub Atomic Agents Integration Plan for Energy Market Intelligence Curriculum

## 1. Architecture Overview

### Key Integration Points
- **Retrieval Systems**: Connect LlamaIndex/Chroma/Neo4j caches in `/root/henry_hub_atomic_agents/shared/chroma_pit_kb` with curriculum knowledge needs
- **Quantitative Analytics**: Tap into `derivation.py`, `lng_forward.py`, and `markets_engine.py` for real market mechanics
- **Data Pipelines**: Leverage `kb_ingest.py` and `emi_alignment.py` for curriculum-relevant chunking
- **Embedding Models**: Use `nomic-embed-text` from HHAA's runtime for semantic search
- **Commodity Fundamentals**: Integrate `fundamentals.py` and `frac_module.py` for empirical market relationships
- **Validation Framework**: Adopt `gatekeeper.py` validation logic for curriculum quality checks

## 2. Integration Implementation

### File Structure Additions
```bash
energy_market_intelligence/
├── HHAA_INTEGRATION_PLAN.md  ← this document
├── scripts/
│   └── retrieve_hhaa_context.py  ← new integration script
└── curriculum/
    └── chapters/
        └── chapter_01/
            └── sections/
                └── section_01/
                    └── content.md  ← to be expanded using integration
```

### `retrieve_hhaa_context.py` Implementation
```python
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
```

## 3. Curriculum Enhancement Strategy

### For Chapter 1 Topics
1. **Storage Dynamics** (section_01):
   - Add quantitative gas storage capacity metrics from `fundamentals.py`
   - Include seasonal storage patterns from `ecmwf_hdd.py`
   - Reference real-world storage depletion rates from `eia_storage.py`

2. **Pipeline Economics** (section_02):
   - Incorporate pressure loss calculations from `frac_module.py`
   - Add compressor station efficiency data from `ngl_term.py`
   - Include historical throughput constraints from `eia_ng_flows.py`

### Validation Workflow
```bash
# After content expansion
/root/.venvs/emi/bin/python3 emi.py test
/root/.venvs/emi/bin/python3 /usr/local/bin/verify_emi.py
```
