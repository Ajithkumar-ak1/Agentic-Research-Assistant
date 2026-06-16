from app.services.llm import llm


def generate_report(
    query,
    findings
):

    prompt = f"""
    Query:
    {query}

    Findings:
    {findings}

    Create a professional report.

    Include:

    1. Executive Summary
    2. Key Findings
    3. Recommendations
    4. Conclusion
    """

    return llm.invoke(prompt).content