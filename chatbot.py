from config import *
import requests
def chat(user_prompt,temperature=TEMPERATURE,url=URL,model=MODEL,API_KEY=API_KEY,system_prompt=SYSTEM_PROMPT):
    headers={
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
    }
    payload={
        "model":model,
        "messages":[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
        ],  
        "temperature": temperature
    }
    response=requests.post(url,json=payload,headers=headers)
    response=response.json()
    result=response['choices'][0]['message']['content']
    return result