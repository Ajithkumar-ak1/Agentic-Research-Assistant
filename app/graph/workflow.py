from langgraph.graph import StateGraph
from app.graph.state import ResearchState
from app.graph.nodes import (
    planner_node,
    researcher_node,
    writer_node
)

builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("researcher", researcher_node)
builder.add_node("writer", writer_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "writer")

graph = builder.compile()