import os
import sys 
import constants

from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Accept query as command-line argument
query =  sys.argv[1]

# Hardcoded loader for demonstration purposes
loader = TextLoader('C:\\Users\\Sharath kumar\\Downloads\\openai-env\\openai-env\\demo\\customers.csv') 
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query, llm=ChatOpenAI()))