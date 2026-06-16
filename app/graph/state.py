from typing import TypedDict, List

class ResearchState(TypedDict):
    query: str
    plan: str
    web_results: List[str]
    findings: str
    report: str