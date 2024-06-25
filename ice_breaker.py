from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from langchain_core.output_parsers import StrOutputParser
import os
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agents import lookup as linkedin_lookup_agent
from third_parties.twitter import scrape_user_tweets
from agents.twitter_lookup_agents import lookup as twitter_lookup_agent


def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    twitter_username = twitter_lookup_agent(name=name)
    twitter_data = scrape_user_tweets(username=twitter_username)

    summary_template = """
    given the Linkedin information {linkedindata} & Twitter Information {twitterdata}  about a person I want you to create:
    1. Name of the Person
    2. A short summary
    3. two interesting facts about them
    4. Location
    5. Number of Tweets 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedindata", "twitterdata"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(
        input={"twitterdata": twitter_data, "linkedindata": linkedin_data}
    )

    print(res)


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with(name="Mrugal Nikhar")
