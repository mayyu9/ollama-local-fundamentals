## 1. Ingest PDF Files
# 2. Extract Text from PDF Files and split into small chunks
# 3. Send the chunks to the embedding model
# 4. Save the embeddings to a vector database
# 5. Perform similarity search on the vector database to find similar documents
# 6. retrieve the similar documents and present them to the user
## run pip install -r requirements.txt to install the required package


from langchain_community.document_loaders import UnstructuredPDFLoader
# from langchain_community.document_loaders import OnlinePDFLoader
import pytesseract
# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_path  = "./data/BOI.pdf"
model = "llama3.2:1b"

# local pdf file upload
if file_path :
    loader = UnstructuredPDFLoader(file_path)
    data = loader.load()
    print("done loading.....")
else:
    print("upload a odf file.")

    # Preview first page
content = data[0].page_content
print(content[:200])

# ==== End of PDF Ingestion ====
