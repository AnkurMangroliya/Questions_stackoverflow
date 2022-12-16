import requests
from bs4 import BeautifulSoup
import pandas as pd

list_stack=[]
page = int(input("Enter page number :"))

for i in range(page):
    base_url=f'https://stackoverflow.com/questions?tab=newest&pagesize={page}'

    r = requests.get(base_url)
    soup = BeautifulSoup(r.content,'html.parser')

    questions = soup.find_all("div",class_="s-post-summary")

    for question in questions:
        s = question.find('h3').text.strip()
        dic ={
            'Question':s
        }
        list_stack.append(dic)

df = pd.DataFrame(list_stack)
df.to_csv('Question_of_stackoverflow.csv')