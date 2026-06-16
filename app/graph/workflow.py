from langgraph.graph import StateGraph, END

from app.graph.state import ResearchState

from app.graph.nodes import (
    supervisor_node,
    planner_node,
    web_node,
    pdf_node,
    research_node,
    evidence_node,
    writer_node
)


def route_after_planner(state):

    web = state["use_web_search"]
    pdf = state["use_pdf_search"]

    if web:
        return "web"

    if pdf:
        return "pdf"

    return "research"


def route_after_web(state):

    if state["use_pdf_search"]:
        return "pdf"

    return "research"


builder = StateGraph(ResearchState)

# Nodes
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
    "evidence",
    evidence_node
)

builder.add_node(
    "writer",
    writer_node
)

# Entry Point
builder.set_entry_point("supervisor")

# Fixed Flow
builder.add_edge(
    "supervisor",
    "planner"
)

# Conditional Routing
builder.add_conditional_edges(
    "planner",
    route_after_planner,
    {
        "web": "web",
        "pdf": "pdf",
        "research": "research"
    }
)

builder.add_conditional_edges(
    "web",
    route_after_web,
    {
        "pdf": "pdf",
        "research": "research"
    }
)

# Remaining Flow
builder.add_edge(
    "pdf",
    "research"
)

builder.add_edge(
    "research",
    "evidence"
)

builder.add_edge(
    "evidence",
    "writer"
)

builder.add_edge(
    "writer",
    END
)

graph = builder.compile()