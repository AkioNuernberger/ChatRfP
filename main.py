import llama_index
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain import OpenAI
#import dotenv
#from dotenv import load_dotenv
#load_dotenv()
import os

os.environ['OPENAI_API_KEY'] = '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'
token = os.environ.get("OPEN-API-KEY")

#Define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="gpt-4")) 
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)



# Define the path to your data directory
data_dir = "/Users/akio/Documents/Test"

# Create a new LlamaIndex
documents = SimpleDirectoryReader (data_dir).load_data()
index = llama_index.GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

# Save your index to a index.json file
index.save_to_disk('index.json')
# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Querying the index
while True:
    prompt = input("Type prompt...")
    response = index.query(prompt)
    response.source_nodes
    print(response)
    print("source nodes", response.source_nodes)
    print("source nodes formatted", response.get_formatted_sources)
    