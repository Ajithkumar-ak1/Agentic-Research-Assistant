from app.services.llm import llm


def decide_route(query: str):

    prompt = f"""
    You are a supervisor agent.

    Analyze the user query.

    Query:
    {query}

    Return ONLY:

    WEB: YES or NO
    PDF: YES or NO
    """

    response = llm.invoke(prompt).content

    use_web = "WEB: YES" in response.upper()
    use_pdf = "PDF: YES" in response.upper()

    return {
        "use_web_search": use_web,
        "use_pdf_search": use_pdf
    }