from langgraph.graph import StateGraph, END

from app.graph.state import ResearchState

from app.graph.nodes import (
    supervisor_node,
    planner_node,
    web_node,
    pdf_node,
    research_node,
    writer_node
)

builder = StateGraph(ResearchState)

builder.add_node(
    "supervisor",
    supervisor_node
)

builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "web",
    web_node
)

builder.add_node(
    "pdf",
    pdf_node
)

builder.add_node(
    "research",
    research_node
)

builder.add_node(
    "writer",
    writer_node
)

builder.set_entry_point("supervisor")

builder.add_edge(
    "supervisor",
    "planner"
)

builder.add_edge(
    "planner",
    "web"
)

builder.add_edge(
    "web",
    "pdf"
)

builder.add_edge(
    "pdf",
    "research"
)

builder.add_edge(
    "research",
    "writer"
)

builder.add_edge(
    "writer",
    END
)

graph = builder.compile()