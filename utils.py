# Import Pacckages
import openai
from dotenv import load_dotenv
import os

# OpenAI Key loading
_ = load_dotenv()
openai.api_key = os.getenv('OpenAI_API_KEY')


def get_sentiment(user_pormpt:str)-> str:
    '''Generate the semtiment of user sentence
    Agrs:
        user_pormpt:str which is the uer sentence want to be classified

    Returns:
        sentemient of the sentence
    '''
    system_prompt = '''You are an AI assiastant which is emtionally inetelegent so your task is to classify user input to ONLY POSITIVE OR NEGATIVE'''

    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_pormpt}
    ]

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
        max_tokens=100
    )
    return response['choices'][0]['message']['content']
