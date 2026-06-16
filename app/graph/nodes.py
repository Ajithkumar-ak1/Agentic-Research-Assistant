from app.agents.supervisor import decide_route
from app.agents.planner import create_plan
from app.agents.researcher import synthesize_research
from app.agents.writer import generate_report

from app.tools.tavily_tool import search_web
from app.agents.pdf_agent import search_pdfs


def supervisor_node(state):

    decision = decide_route(
        state["query"]
    )

    state.update(decision)

    return state


def planner_node(state):

    state["plan"] = create_plan(
        state["query"]
    )

    return state


def web_node(state):

    if state["use_web_search"]:

        state["web_results"] = search_web(
            state["query"]
        )

        for result in state["web_results"]:

            state["sources"].append(
                {
                    "title": result["title"],
                    "url": result["url"],
                    "type": "web"
                }
            )

    return state


def pdf_node(state):

    if state["use_pdf_search"]:

        state["pdf_results"] = search_pdfs()

        for pdf in state["pdf_results"]:

            state["sources"].append(
                {
                    "title": pdf["title"],
                    "type": "pdf"
                }
            )

    return state


def research_node(state):

    state["findings"] = synthesize_research(
        state["query"],
        state["web_results"],
        state["pdf_results"]
    )

    return state


def writer_node(state):

    state["report"] = generate_report(
        state["query"],
        state["findings"]
    )

    return state