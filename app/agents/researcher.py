from app.tools.tavily_tool import search_web

def conduct_research(query: str):

    results = search_web(query)

    context = []

    for r in results:
        context.append(
            f"""
            Title: {r['title']}
            Content: {r['content']}
            URL: {r['url']}
            """
        )

    return "\n\n".join(context)