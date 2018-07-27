#test DICT python
import random
import dialogflow as df

val = 'oil price'

@app.route('/dialogflow', methods=['POST'])
def dialogflow():
    msg_in_json = requests.get_json()
    msg_in_str = json.dumps(msg_in_json)
    reply()
    #replyToken = msg_in_json["events"][0]['replyToken']
    #what did i do ?
    return 'OK', 200

def reply(text):
    Dialogflow_API = 'https://api.dialogflow.com/v1/query?v=20150910'
    headers = {
        'Authorization': DIALOGFLOW_API_KEY,
        'Content-Type': 'application/json'
        }
    body = json.dumps({
        "contexts": some_list_of_context,
        "lang": "en",
        "query": msgs,
        "sessionId": "12345"
        "timezone": "America/New_York"
        })
    msgs = 'hello'
    requests.post(Dialogflow_API,headers=headers, data=body)
    return
