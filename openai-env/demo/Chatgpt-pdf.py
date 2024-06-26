import os
import sys 
import constants

from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader

# Define the function to get the appropriate loader for a given file
def get_loader_for_file(filepath):
    # Check the file extension
    _, ext = os.path.splitext(filepath)
    
    if ext.lower() == '.pdf':
        return PyPDFLoader(filepath)
    elif ext.lower() in ['.csv', '.txt']:
        # For CSV and TXT files, you can directly return the TextLoader
        return TextLoader(filepath)
    else:
        raise ValueError(f"No loader available for file type: {ext}")

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Accept query as command-line argument
query =  sys.argv[1]

# Hardcoded file path for demonstration purposes
file_path = 'C:\\Users\\Sharath kumar\\Downloads\\openai-env\\openai-env\\demo\\SalesforceUserGuide.pdf'

# Get the appropriate loader for the file
loader = get_loader_for_file(file_path)

# Create an index using the loader
index = VectorstoreIndexCreator().from_loaders([loader])

# Perform the query and print the result
print(index.query(query, llm=ChatOpenAI()))




#'C://Users//Sharath kumar//Downloads//openai-env//openai-env//demo//SalesforceUserGuide.pdf'