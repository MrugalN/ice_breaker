from typing import List, Dict, Any

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    name: str = Field(description="Name of the Person")
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    location: str = Field(description="location")
    num_tweets: str = Field(description="Number of Tweets")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "summary": self.summary,
            "facts": self.facts,
            "location": self.location,
            "Number of Tweets": self.num_tweets,
        }


summary_parser = PydanticOutputParser(pydantic_object=Summary)
