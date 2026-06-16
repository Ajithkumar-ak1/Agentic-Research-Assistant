from app.services.llm import llm


def synthesize_research(
    query,
    web_results,
    pdf_results
):

    context = ""

    for item in web_results:

        context += f"""
        WEB SOURCE

        Title:
        {item['title']}

        Content:
        {item['content']}
        """

    for item in pdf_results:

        context += f"""
        PDF SOURCE

        Title:
        {item['title']}

        Content:
        {item['content']}
        """

    prompt = f"""
    Query:
    {query}

    Sources:
    {context}

    Create structured findings.
    """

    return llm.invoke(prompt).content