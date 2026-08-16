#simple example of structured output with schema

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()
model= ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)
#schema
class Review(TypedDict):
    summary:Annotated[str, "A brief summary of the movie review"]
    sentiment:Annotated[str, "Return the sentiment of the movie review"]

structured_mode=model.with_structured_output(Review)

result=structured_mode.invoke("The movie has a gripping story, strong performances, and impressive visuals, following a character who overcomes challenges while discovering the importance of friendship and courage. Overall, it is entertaining and emotionally engaging")
print(result)
print(result['summary'])
print(result['sentiment'])