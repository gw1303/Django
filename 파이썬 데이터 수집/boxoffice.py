import requests
import json
from datetime import datetime, timedelta
import pandas as pd

api_key = '*'

target_time = datetime(2019, 6, 16)
res_time = '20190616'

audiAcc = []  # 누적관객
movieCd = []  # 영화코드
movieNm = []  # 영화이름

for i in range(1,51) :
    
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key='+api_key+'&targetDt='+res_time+'&weekGb=0'     

    target_time = target_time + timedelta(weeks=1)
    res_time = str(target_time)[:10].replace('-', '')
    
    headers = {'Content-Type': 'application/json; charset=utf-8'} 
    cookies = {'session_id': 'sorryidontcare'} 
    res = requests.get(url, headers=headers, cookies=cookies)

    res = res.json()
    
    for i in res['boxOfficeResult']['weeklyBoxOfficeList'] :
        audiAcc.append(i['audiAcc'])  # 누적관객
        movieCd.append(i['movieCd'])  # 영화코드
        movieNm.append(i['movieNm'])  # 영화이름

        
df = pd.DataFrame(columns=['movieCd','movieNm','audiAcc'])
df['movieCd'] = movieCd
df['movieNm'] = movieNm
df['audiAcc'] = audiAcc

# 최근의 누적관객수만 남기고 중복 제거
df.drop_duplicates(subset='movieCd', keep='last', inplace=True) 
# 누적관객수 타입을 int로
df['audiAcc'] = df['audiAcc'].astype('int')
# 누적관객수 기준 내림차순 정렬
df.sort_values('audiAcc', ascending=False, inplace=True)
# 인덱스 초기화
df.reset_index(drop=True, inplace=True)


# csv 저장
df.to_csv('boxoffice.csv', encoding='euc-kr')