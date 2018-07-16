from flask import Flask, request
import json
import requests
import regex
from zeep import Client
from lxml import etree
# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer zWj79zc/UZsA5V1QaJqTQVTaFhDAjsfMQFQiD4DBOnHBT4DlVJRiv9ltpf0jeWQ3j+nbmrzySep65t+lEvPEI4tcsI129cVzsh6AoispDi9u/t0zOIgdW2v/wmy+mgPOrtDX42X7Rg33klsUmqUxBAdB04t89/1O/w1cDnyilFU='
#ptt_api setup
ptt_api = Client('http://www.pttplc.com/webservice/pttinfo.asmx?WSDL')
ptt_result = ptt_api.service.CurrentOilPrice("en")
ptt_data = etree.fromstring(ptt_result)


#function must declare under this line otherwise app will crash
app = Flask(__name__)

@app.route('/')
def index():
    #ptt_data_list = cleanhtml(ptt_result)
    #ptt_data_list = ptt_data_list.split()
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', ptt_result)
    return cleantext
@app.route('/bot', methods=['POST'])

def bot():
    
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    
    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    userID =  msg_in_json["events"][0]['source']['userId']
    msgType =  msg_in_json["events"][0]['message']['type']
    
    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    if msgType != 'text':
        reply(replyToken, ['Only text is allowed.'])
        return 'OK',200
    
    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ 
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    text = msg_in_json["events"][0]['message']['text'].lower().strip()
    
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ exact match
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # if text in response_dict:
    #     replyQueue.append(reponse_dict[text])
    # else:
    #     replyQueue.append('ไม่รู้ว่าจะตอบอะไรดี TT')
       
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ non-exact match
    # โดยที่มี method ชื่อ find_closest_sentence ที่ใช้การเปรียบเทียบประโยค
    # เพื่อค้นหาประโยคที่ใกล้เคียงที่สุด อาจใช้เรื่องของ word embedding มาใช้งานได้ครับ
    # simple sentence embeddings --> https://openreview.net/pdf?id=SyK00v5xx
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # closest = find_closest_sentence(response_dict, text)
    # replyQueue.append(reponse_dict[closest])
   
    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    replyQueue.append('นี่คือรูปแบบข้อความที่รับส่ง')
    #replayQueue.append(ptt_result)
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    replyQueue.append(msg_in_string)
    reply(replyToken, replyQueue[:])
    
    return 'OK', 200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


if __name__ == '__main__':
    app.run()
