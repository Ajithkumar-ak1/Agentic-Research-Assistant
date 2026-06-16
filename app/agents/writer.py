from app.services.llm import llm


def generate_report(
    query,
    findings,
    evidence,
    sources
):

    formatted_sources = "\n".join(
        [
            f"[{s['id']}] {s['title']} - {s.get('url', '')}"
            for s in sources
        ]
    )
    
    prompt = f"""
    Query:
    {query}

    Findings:
    {findings}

    Evidence:
    {evidence}

    Available Sources:
    {sources}

    Generate a professional research report.

    Rules:
    - Use ONLY the provided evidence.
    - Every factual claim must include a citation.
    - Citations must use the source ID format [1], [2], etc.
    - Do not invent citations.
    - Do not cite sources that are not provided.

    Structure:

    # Executive Summary

    # Key Findings

    # Evidence-Based Analysis

    # Recommendations

    # Conclusion

    # References
    """
    
    return llm.invoke(prompt).content