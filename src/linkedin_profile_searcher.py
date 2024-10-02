from typing import Any, Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate 
from langchain_ollama import ChatOllama
from agents.linkedin_lookup_agent import lookup
from service.linkedin import scrape_linkedin_profile
from entities.summary import summary_parser, Summary


def search_profile(name:str ) -> Tuple[Summary, str]:

    linkedin_url = lookup(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=False)

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    
    YOU MUST RESPONDE JSON FORMAT, NOTHING MORE
    
    \n{format_instructions}
    """
    summary = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    llm = ChatOllama(model='llama3.2', temperature=0)

    chain = summary | llm | summary_parser
    print('ya tengo todos los datos, llamo a la IA')
    res:Summary = chain.invoke(input={'information': linkedin_data})
    print(res)
    return res, linkedin_data.get("profile_pic_url")

if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    print(search_profile('Bill Gates'))