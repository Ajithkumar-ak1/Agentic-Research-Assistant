from typing import TypedDict, List, Dict

class ResearchState(TypedDict):
    query: str
    plan: str

    use_web_search: bool
    use_pdf_search: bool

    web_results: List[Dict]
    pdf_results: List[Dict]

    findings: str

    sources: List[Dict]

    report: str