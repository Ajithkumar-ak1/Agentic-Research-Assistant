from app.services.llm import llm

def generate_report(query, research):

    prompt = f"""
    Research Query:
    {query}

    Findings:
    {research}

    Create a professional report.

    Include:

    1. Executive Summary
    2. Key Findings
    3. Trends
    4. Recommendations
    5. Sources
    """

    return llm.invoke(prompt).content