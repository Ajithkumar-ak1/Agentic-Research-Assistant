from app.services.llm import llm


def extract_evidence(query, sources):

    context = ""

    for source in sources:

        context += f"""
        Source ID: {source['id']}
        Title: {source['title']}
        Content:
        {source.get('content', '')}
        """

    prompt = f"""
    Query:
    {query}

    Sources:
    {context}

    Extract key findings.

    For every finding provide:

    CLAIM:
    SOURCE_ID:
    """

    return llm.invoke(prompt).content