from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



from backend.schemas.trip import ChatRequest, ChatResponse

from backend.agent.planner import agent_think



@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = agent_think(req.session_id, req.message)
    return {"response": result}
