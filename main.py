from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv(".env", verbose=True)



llm = OpenAI()

result = llm.invoke("안녕?")
print(result)
