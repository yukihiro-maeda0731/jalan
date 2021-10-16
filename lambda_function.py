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
        # シーケンスデータを得る
        seqtable = dynamoDB.Table('Sequence')
        nextseq = get_next_seq(seqtable, 'Comments')
        table.put_item(
            Item = {
                'id' : nextseq,
                'comment': item.text,
            }
        )
        print('クチコミをDBに登録しました')

# 連番を裁判して返す関数
def get_next_seq(table, tablename):
	response = table.update_item(
		Key = {
			'tablename' : tablename
		},
		UpdateExpression='set seq = seq + :val',
		ExpressionAttributeValues = {
			':val' : 1
		},
		ReturnValues='UPDATED_NEW'
	)
	return response['Attributes']['seq']