from fastapi import FastAPI
import google.generativeai as genai
from pydantic import BaseModel

genai.configure(api_key="AIzaSyBDqOhWlvNqG9Crmb7Ip01vNYtMSHKtx1A")

app = FastAPI()


def read(message):
    res=""
    for chunk in message:
        chunk.text.replace('*',"")
        res=res+chunk.text
    return {"res":res}


model=genai.GenerativeModel("gemini-pro")

history=[]
chat=model.start_chat(history=history)

chat.send_message("your name is kate.I want you to respond to my every question in few lines.")

def chatting(text):
    try:
        print(f"inside try {text}")
        res=chat.send_message(text)
        # print(res)
        return read(res)
        # return {"res":res}
    except:
        print(text)
        return {"Error": "Harmfull words found in the chat. Please try again"}

class TextMessages(BaseModel):
    message:str


@app.get('/')
def home():
    return {"message": "welcome, I am Kate"}

@app.post('/chat')
def sendtext(mes:TextMessages):
    return chatting(mes.message)

