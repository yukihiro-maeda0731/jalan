import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    r = requests.get("https://www.jalan.net/yad330474/kuchikomi/?screenId=UWW3001&yadNo=330474&smlCd=012102&distCd=01")
    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    all=soup.find_all("p",{"class":"jlnpc-kuchikomiCassette__postBody"})

    l=[]
    for item in all:
        d={}
        d["クチコミ"]=item.text
        l.append(d)
        print(l)