# ollama-local-fundamentals

https://bounteous.udemy.com/course/master-ollama-python/learn/lecture/46411613#questions

Python venv activation
How you activate your virtual environment depends on the OS you’re using.

Windows venv activation
To activate your venv on Windows, you need to run a script that gets installed by venv. If you created your venv in a directory called myenv, the command would be:

# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1

# intall the requirements
pip install -r .\requirements.txt

# fix for poppler and Tesseract-OCR
1. install poppler, system level and set the environment variable path for poppler
2. install Tesseract-ocr, system level and virtual environment
3. set Tesseract-ocr in path 
4. pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
