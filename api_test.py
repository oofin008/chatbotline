from linebot import LineBotApi
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('<zWj79zc/UZsA5V1QaJqTQVTaFhDAjsfMQFQiD4DBOnHBT4DlVJRiv9ltpf0jeWQ3j+nbmrzySep65t+lEvPEI4tcsI129cVzsh6AoispDi9u/t0zOIgdW2v/wmy+mgPOrtDX42X7Rg33klsUmqUxBAdB04t89/1O/w1cDnyilFU=>')

try:
    profile = line_bot_api.get_profile('<user_id>')
    print(profile.display_name)
    print(profile.user_id)
except LineBotApiError as e:
    print('Wow, you got error')
