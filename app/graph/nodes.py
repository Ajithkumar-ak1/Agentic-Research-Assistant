from app.agents.planner import create_plan
from app.agents.researcher import conduct_research
from app.agents.writer import generate_report

def planner_node(state):

    state["plan"] = create_plan(state["query"])

    return state


def researcher_node(state):

    state["findings"] = conduct_research(
        state["query"]
    )

    return state


def writer_node(state):

    state["report"] = generate_report(
        state["query"],
        state["findings"]
    )

    return state