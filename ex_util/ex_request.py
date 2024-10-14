import requests
url = "http://127.0.0.1:8080/api/addCode"
# post 보낼 데이터
data = {
    "commCd" : "AB01"
    ,"commNm" : "Test"
    ,"commOrd" : 1
}
# 요청 헤더 JSON
headers = {"content-Type" : "application/json"}
res = requests.post(url, json=data, headers=headers)
print(f"status code:{res.status_code}")
res.encoding = "utf-8"
print(f"body: {res.text}")