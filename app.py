## converting blog graph calls to api 

import uvicorn 
from fastapi import FastAPI , Request
import asyncio
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("LANGCHAIN_API_KEY"))

app = FastAPI()

os.environ["LANGCHAIN_TRACING"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Blog_Generation_v1"


## API's

@app.post("/blogs")  # api req

# async method
async def create_blogs(request:Request):
    data = await request.json()
    topic = data.get("topic" , "")
    language = data.get("language" , "")
    
    ## get llm object 
    
    groqllm =GroqLLM()
    llm = groqllm.get_llm()
    
    ## get the graph
    
    graph_builder  = GraphBuilder(llm)
    if topic and language:
        graph = graph_builder.setup_graph(usecase="language")
        state = graph.invoke({"topic":topic , "current_language":language.lower()})
        
    elif topic:
        graph = graph_builder.setup_graph(usecase="topic")
        state = graph.invoke({"topic":topic})
    
        
    return {"data":state}
    

## 0.0.0.0 is referring to local host


## we test this api in postman

if __name__ == "__main__":
    uvicorn.run("app:app" , host = "0.0.0.0",
                port = 8000,
                reload=True)
    
    
