import os
import sys 
import constants

from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = "Tell me the contents of the file?"
#loader = DirectoryLoader("./demo/", glob="*.txt")
loader = TextLoader('C:\\Users\\Sharath kumar\\Downloads\\openai-env\\openai-env\\demo\\SalesforceUserGuide.pdf')
index = VectorstoreIndexCreator().from_loaders([loader])

#print(index.query(query, llm=ChatOpenAI()))
try:
    result = index.query(query, llm=ChatOpenAI())
    print(result)
except Exception as e:
    print("An error occurred:", e)
###################################################################################
#chat_model = ChatOpenAI(openai_api_key=constants.APIKEY)

#result = chat_model.predict("Why should I learn python!")
#print(result)
###################################################################################

# https://www.youtube.com/watch?v=9AXP7tCI9PI
# https://www.youtube.com/watch?v=mrjq3lFz23s

#https://www.langchain.com/langchain
#https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.airbyte.AirbyteSalesforceLoader.html

# https://www.youtube.com/watch?v=D8K-x4oEyMU
# https://www.langchain.com/langchain