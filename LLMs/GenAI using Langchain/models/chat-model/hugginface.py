from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324",
    task="text-generation",
    provider="auto",
)

model=ChatHuggingFace(llm=llm)
result=model.invoke("when is casual masking applied in the transformer architecture?")
print(result.content)