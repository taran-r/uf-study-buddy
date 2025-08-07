import openai
import os
import json

def configure_openai():
    key_file = r"your_file_path"

    with open(key_file, 'r') as file:
        data = json.load(file)

    OPENAI_API_KEY = data.get('OPENAI_API_KEY')
    base_url = data.get('base_url')

    os.environ['TOOLKIT_API_KEY'] = OPENAI_API_KEY

    openai_client = openai.OpenAI(
        api_key=OPENAI_API_KEY,
        base_url=base_url
    )
    
    return openai_client
