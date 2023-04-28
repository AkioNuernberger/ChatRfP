import llama_index

# Define the path to your data directory
data_dir = "/path/to/data/directory"

# Create a new LlamaIndex
index = llama_index.Index()

# Define the file formats you want to index
file_formats = ["docx", "xlsx", "pdf", "txt"]

# Index the documents in your data directory
for file_format in file_formats:
    index.add_directory(data_dir, file_format)

# Search for documents in the index
results = index.search("your search query")
for result in results:
    # Print the file path and score for each result
    print(result["path"], result["score"])
