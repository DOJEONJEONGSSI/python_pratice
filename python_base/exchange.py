import requests
# 현재 환율 api
# USD 1달러 기준 각 국가의 환율정보 json으로 리턴



def fn_to_krw(usd):
    url = "http://open.er-api.com/v6/latest/USD"
    res = requests.get(url)
    data = res.json()
    krw = data['rates']['KRW']
    return usd * krw


if __name__ == '__main__':
    # 달러 to 한화 함수를 작성해주세요
    # input : 달러 금액   (ex: 10)
    # output : 원화 금액  (ex:13421.04544)
    usd = 220.91
    print("%d 달러는 한화로 %.2f"% (usd,fn_to_krw(usd)))