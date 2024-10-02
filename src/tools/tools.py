from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """ Searches for Linkedin or Twitter Profile Page """
    
    search: TavilySearchResults = TavilySearchResults()
    res = search.run(f"{name} Linkedin")
    url = res[0]['url']
    #url="https://www.linkedin.com/in/williamhgates"
    return url