from app.services.llm import llm

def create_plan(query: str):

    prompt = f"""
    Create a research plan.

    Query:
    {query}

    Return:
    - objectives
    - search strategy
    - expected outcome
    """

    return llm.invoke(prompt).content