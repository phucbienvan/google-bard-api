from bardapi import Bard
import os
from dotenv import load_dotenv
import requests
load_dotenv()
token= os.environ['_BARD_API_KEY']

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        } 
session.cookies.set("__Secure-1PSID", token) 
bard = Bard(token=token, session=session, timeout=30)
data = bard.get_answer("thời tiết đà nẵng ngày mai")['content']

print(data)
