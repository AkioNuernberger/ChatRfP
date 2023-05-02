import llama_index
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
#import dotenv
#from dotenv import load_dotenv
#load_dotenv()
import os

os.environ['OPENAI_API_KEY'] = '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'
token = os.environ.get("OPEN-API-KEY")


# Define the path to your data directory
data_dir = "/Users/akio/Documents/Test"

# Create a new LlamaIndex
documents = SimpleDirectoryReader (data_dir).load_data()
index = llama_index.GPTSimpleVectorIndex.from_documents(documents)

#Search for documents in the index
#results = index.search("your search query")
#for result in results:
    # Print the file path and score for each result
    #print(result["path"], result["score"])

# load gdocs and index them 
#documents = loader.load_data(document_ids=gdoc_ids)
#whatindex = GPTSimpleVectorIndex(documents)

# Save your index to a index.json file
index.save_to_disk('index.json')
# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Querying the index
while True:
    prompt = input("Type prompt...")
    response = index.query(prompt)
    print(response)
    