from app.agents.supervisor import decide_route
from app.agents.planner import create_plan
from app.agents.researcher import synthesize_research
from app.agents.writer import generate_report
from app.agents.evidence_agent import extract_evidence
from app.tools.tavily_tool import search_web
from app.agents.pdf_agent import search_pdfs


def supervisor_node(state):

    decision = decide_route(
        state["query"]
    )

    state.update(decision)

    state["trace"].append(
        f"Supervisor: Web={decision['use_web_search']} PDF={decision['use_pdf_search']}"
    )

    return state

def planner_node(state):

    state["plan"] = create_plan(
        state["query"]
    )

    state["trace"].append(
        "Planner: Research plan generated"
    )

    return state


def web_node(state):

    if state["use_web_search"]:

        results = search_web(
            state["query"]
        )

        state["web_results"] = results

        state["trace"].append(
            f"Web Agent: Retrieved {len(results)} sources"
        )

    return state


def pdf_node(state):

    if state["use_pdf_search"]:

        pdfs = search_pdfs()

        state["pdf_results"] = pdfs

        state["trace"].append(
            f"PDF Agent: Found {len(pdfs)} PDFs"
        )

    return state

def research_node(state):

    state["findings"] = synthesize_research(
        state["query"],
        state["web_results"],
        state["pdf_results"]
    )
    state["trace"].append(
    "Research Agent: Findings synthesized"
)

    return state


def writer_node(state):

    state["report"] = generate_report(
        state["query"],
        state["findings"],
        state["evidence"],
        state["sources"]
    )

    state["trace"].append(
    "Writer Agent: Final report generated"
)

    return state



def evidence_node(state):

    state["evidence"] = extract_evidence(
        state["query"],
        state["sources"]
    )

    return state