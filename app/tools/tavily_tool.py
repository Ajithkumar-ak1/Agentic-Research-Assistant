from tavily import TavilyClient
from app.core.config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query: str):

    results = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return results["results"]