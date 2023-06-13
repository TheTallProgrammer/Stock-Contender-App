import openai
import os
from packages.backend.progress_tracker.global_instance import progress_tracker

messages = [{"role": "system", "content": "You are an intelligent AI stock broker with lots of insight and wisdom."}]

def receive_input(message): 
    messages.append({"role": "user", "content": message},)
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    progress_tracker.register_task()
    
    return reply


def validate_api_key(api_key):
    try:
        # Save the organization ID and API key
        openai.api_key = api_key
        
        # Try making a simple API request
        openai.Model.list()
        # If the above line did not raise an exception, then the organization ID and API key are valid
        return True
        
    except Exception as e:
        # If an exception was raised, then the organization ID or API key is probably invalid
        raise e # Raise the exception again so it can be caught and handled in the UI