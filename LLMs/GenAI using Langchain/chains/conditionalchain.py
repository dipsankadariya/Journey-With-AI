from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
load_dotenv()

model1=ChatGroq(model="llama-3.1-8b-instant")

class FeedbackSentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback, either positive or negative.")


parser=PydanticOutputParser(pydantic_object=FeedbackSentiment)
parser2=StrOutputParser()

prompt1=PromptTemplate(
    template= "Classfiy the sentiment of the following text as positive or negative, : {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser.get_format_instructions() }
)

classifier_chain=prompt1 | model1 | parser

classifier_with_feedback = RunnableParallel(
    feedback=lambda x: x["feedback"],
    sentiment=classifier_chain,
)

prompt2=PromptTemplate(
    template="Generate a response to the following positive {feedback}.",
    input_variables=["feedback"]
)
prompt3=PromptTemplate(
    template="Generate a response to the following negative {feedback}.",
    input_variables=["feedback"]
)

branch_chain=RunnableBranch(
    (lambda x: x["sentiment"].sentiment == "positive", prompt2 | model1 | parser2),
    (lambda x: x["sentiment"].sentiment == "negative", prompt3 | model1 | parser2),
    RunnableLambda(lambda x: "no sentiment detected.")
)

final_chain= classifier_with_feedback | branch_chain
result=final_chain.invoke({"feedback":"I love this product! It has exceeded my expectations."})
print(result)
