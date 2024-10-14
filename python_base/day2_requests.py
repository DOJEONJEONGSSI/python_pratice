'''
    requests는 파이썬에서 HTTP요청을 쉽게 보낼 수 있도록 해주는 라이브러리
    주로 웹사이트나 API와 통신할 때 사용됨.
     - GET, POST, PUT, DELETE 요청 처리
     - 응답 내용 파싱 : json or text 형태로.
     - 요청 시 자동으로 URL 인코딩 처리
     - 예외처리 (http요청 중 발생할 수 있는 오류에 대해 예외 처리를 제공)
'''
import requests
# 없다면 pip install requests
# url = "https://api.upbit.com/v1/market/all"
# res = requests.get(url)
# if res.status_code == 200:
#     data = res.json() # json 형태로 파싱
#     for v in data:
#         print(v['korean_name'], v['market'])


def fn_get_coin_price(code):
    url = f"https://api.upbit.com/v1/ticker?markets={code}"
    res = requests.get(url)
    price = 0
    if res.status_code == 200:
        data = res.json()  # json 형태로 파싱
        price = data[0]['trade_price']
    return price

# 현재시세 가져오는 함수.
# input : market(코인 코드)
# output: 현재 시장가 trade_price
# ex : https://api.upbit.com/v1/ticker?markets=KRW-BTC
print(fn_get_coin_price('KRW-BTC'))
print(fn_get_coin_price('KRW-ETH'))


