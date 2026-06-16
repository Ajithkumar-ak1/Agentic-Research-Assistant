from fastapi import APIRouter
import time

from app.api.schemas import ResearchRequest
from app.graph.workflow import graph

router = APIRouter()

@router.post("/research")
async def research(req: ResearchRequest):

    start = time.time()

    result = graph.invoke(
        {
            "query": req.query,
            "plan": "",
            "web_results": [],
            "findings": "",
            "report": ""
        }
    )

    execution_time = round(time.time() - start, 2)

    return {
        "query": req.query,
        "plan": result["plan"],
        "report": result["report"],
        "execution_time": execution_time
    }