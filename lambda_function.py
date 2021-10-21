import requests
from bs4 import BeautifulSoup
import boto3
dynamoDB = boto3.resource('dynamodb')
table= dynamoDB.Table('Comments')

def lambda_handler(event,context):
    
    r = requests.get("https://www.jalan.net/yad330474/kuchikomi/?screenId=UWW3001&yadNo=330474&smlCd=012102&distCd=01")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all=soup.find_all("p",{"class":"jlnpc-kuchikomiCassette__postBody"})

    for item in all:
        print(item.text)

