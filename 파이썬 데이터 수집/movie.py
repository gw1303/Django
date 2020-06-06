import requests
import json
import pandas as pd

api_key = '*'

# 영화 정보 크롤링
movieCd = [] # 영화 대표코드
movieNm = [] # 영화명(국문)
movieNmEn = [] # 영화명(영문)
movieNmOg = [] # 영화명(원문)
watchGradeNm = [] # 관람등급
openDt = [] # 개봉연도
showTm = [] # 상영시간
genreNm = [] # 장르
peopleNm = [] # 감독명

for movie_code in df['movieCd'] :

    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={api_key}&movieCd={movie_code}'

    res = requests.get(url)
    res = res.json()
    
    movieCd.append(res['movieInfoResult']['movieInfo']['movieCd']) # 영화 대표코드
    movieNm.append(res['movieInfoResult']['movieInfo']['movieNm']) # 영화명(국문)
    movieNmEn.append(res['movieInfoResult']['movieInfo']['movieNmEn']) # 영화명(영문)
    movieNmOg.append(res['movieInfoResult']['movieInfo']['movieNmOg']) # 영화명(원문)
    watchGradeNm.append(res['movieInfoResult']['movieInfo']['audits']) # 관람등급
    openDt.append(res['movieInfoResult']['movieInfo']['openDt']) # 개봉연도
    showTm.append(res['movieInfoResult']['movieInfo']['showTm']) # 상영시간
    genreNm.append(res['movieInfoResult']['movieInfo']['genres']) # 장르
    peopleNm.append(res['movieInfoResult']['movieInfo']['directors']) # 감독명
    
# 데이터 프래임 생성
movie_df = pd.DataFrame(columns=['movieCd','movieNm','movieNmEn','movieNmOg','watchGradeNm','openDt','showTm','genreNm','peopleNm'])

movie_df['movieCd'] = movieCd # 영화 대표코드
movie_df['movieNm'] = movieNm# 영화명(국문)
movie_df['movieNmEn'] = movieNmEn # 영화명(영문)
movie_df['movieNmOg'] = movieNmOg  # 영화명(원문)
movie_df['watchGradeNm'] = watchGradeNm  # 관람등급
movie_df['openDt'] = openDt  # 개봉연도
movie_df['showTm'] = showTm  # 상영시간
movie_df['genreNm'] = genreNm # 장르
movie_df['peopleNm'] = peopleNm # 감독명
movie_df

peopleNm = []
watchGradeNm = []
genreNm = []

# 감독이름 추출
for i in movie_df['peopleNm'] :
    r = []
    if len(i) != 0 :
        peopleNm.append(i[0]['peopleNm'])
    else :
        peopleNm.append('None')
# 등급 추출
for i in movie_df['watchGradeNm'] :
    r = []
    if len(i) != 0 :
        watchGradeNm.append(i[0]['watchGradeNm'])
    else :
        watchGradeNm.append('None')
# 장르 추출    
for i in movie_df['genreNm'] :
    r = []
    for j in range(len(i)) :
        r.append(i[j]['genreNm'])
    genreNm.append(' '.join(r))
    
movie_df['watchGradeNm'] = watchGradeNm  # 관람등급
movie_df['genreNm'] = genreNm # 장르
movie_df['peopleNm'] = peopleNm # 감독명

movie_df

# csv 저장
movie_df.to_csv('movie.csv', encoding='utf-8')