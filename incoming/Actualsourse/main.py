from fastapi import FastAPI, Query
from pydantic import BaseModel
from pathlib import Path
import re
from .packages.core.rag_pgvector_simulator import pgvector_rag_search, initialize_rag_system

app = FastAPI(title="Iskra API", version="1.0.0")

# The tokenize function is no longer needed for the vector search, but kept for reference.
# def tokenize(s: str): return re.findall(r"[a-zA-Zа-яА-Я0-9_]+", s.lower())

class Citation(BaseModel):
    source: str
    snippet: str

class SearchResponse(BaseModel):
    query: str
    citations: list[Citation]
    delta: dict

# Replaced with pgvector_rag_search
# def search_files(q: str, root: Path, limit=5):
#     qtok = set(tokenize(q)); hits=[]
#     for p in root.iterdir():
#         if p.suffix.lower() in {'.md','.txt'} and p.is_file():
#             txt = p.read_text(encoding='utf-8', errors='ignore')
#             toks=set(tokenize(txt)); score=len(qtok & toks)
#             if score>0: hits.append((score, p.name, txt[:240].replace('\n',' ')))
#     hits.sort(key=lambda x: x[0], reverse=True)
#     return [{'source':h[1],'snippet':h[2]} for h in hits[:limit]]

@app.on_event("startup")
async def startup_event():
    # Initialize the RAG system with the project's document root
    # In a real deployment, this would connect to the pgvector database
    initialize_rag_system(Path("/home/ubuntu/project_audit/iskra_kanon"))

@app.post('/v1/search', response_model=SearchResponse)
def v1_search(q: str = Query(...)):
    citations, omega = pgvector_rag_search(q)
    # The Omega (Ω) value is now dynamically calculated based on vector similarity
    return {'query': q, 'citations': citations, 'delta': {'∆':'search','Ω': omega,'Λ':'none'}}

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    message: str
    citations: list[Citation]
    delta: dict

@app.post('/v1/chat', response_model=ChatResponse)
def v1_chat(req: ChatRequest):
    citations, omega = pgvector_rag_search(req.message)
    # The Omega (Ω) value is now dynamically calculated based on vector similarity
    return {'message': 'Скелет ответа', 'citations': citations, 'delta': {'∆':'chat','Ω': omega,'Λ':'none'}}
