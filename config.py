import os
from dotenv import load_dotenv
load_dotenv()

# AI model config
API_KEY=os.getenv('API_KEY')
SYSTEM_PROMPT="""
You're required to write a persuasive message for a lead. We're offering service in SEO and Web dev (infer which one to offer based on data).
You'll be given some data about them. Write a message based on this template.
Hi (local bussiness name) , I came across your Website Profile & Noticed that your Local ranking might not be fully optimized on Google. I also checked out your top 3 Competitors, and they’re currently outperforming you and likely getting more LEADS of  Car bookings in (city name)(without Expensive ADS).
P.S. : I Recorded a Quick video showing what’s hurting your rankings and how to fix it.(just trying help) mind if share it with you?
Don't use markdown syntax because that doesn't render on whatsapp. Don't use emojis. Just give the message itself and output and nothing else. As in, don't start with Sure here's a persuasive message.... or something"""
USER_PROMPT=""""""
MODEL='deepseek-chat'
URL="https://api.deepseek.com/v1/chat/completions"
TEMPERATURE=0.0

data_path=r"data.xlsx"