import os

class Config:
    APP_DIR = os.path.join(os.path.abspath(os.curdir))
    WORK_DIR = os.path.join(APP_DIR, 'app')
    RAG_DIR = os.path.join(os.sep, WORK_DIR, 'knowledge')
    VECTORSTORE_PATH = os.path.join(os.sep, RAG_DIR, 'vectorstore')

    DATA_FILE_NAME = f"accessibility_data_with_text.csv"
    DATA_PATH =  os.path.join(os.sep, RAG_DIR, DATA_FILE_NAME)

    MODEL = 'gemini-2.0-flash'
    TEMPERATURE = 0.4
