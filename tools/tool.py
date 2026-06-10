from tavily import TavilyClient
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# ================= API KEY =================
tavily_api_key = os.getenv("TAVILY_API_KEY")

if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY not found")

tavily = TavilyClient(api_key=tavily_api_key)

# ================= SEARCH =================
def web_search(query: str):
    result = tavily.search(query=query,   
                           days=7,
                           search_depth="basic",
                           max_results=3,
                           include_raw_content=False)
    return result["results"]




# beautiful soup
def fetch_url(url: str) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(separator=" ", strip=True)[:2000]

    except Exception as e:
        return f"Error fetching URL: {str(e)}"