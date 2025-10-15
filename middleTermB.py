import requests
import pandas as pd

# 1-2. Python을 사용하여 API를 호출하는 코드를 작성하고,
# 2015년 1월부터 2024년 12월까지의 개인 유형의 현년 전기, 가스, 수도, 지역난방 에너지 사용량 데이터를 수집하는 프로그램을 작성하시오.
# API 호출 성공을 확인할 수 있는 실행 결과를 캡처하여 첨부하시오. (7점)
# 문제의 조건인 '개인 유형'을 코드내역.xlsx 파일의 두번째 sheet인 회원 타입에서 '회원유형'에서 '개인(일반)'으로 간주함.

def get_year_months():
    year_months = list()
    for year in range(2015, 2025):
        for month in range(1, 13):
            if month < 10:
                month = '0' + str(month)
            year_months.append(f'{year}/{month}')
    return year_months

result = list()

for year_month in get_year_months():
    url = f'http://openapi.seoul.go.kr:8088/58474744486c6f67393777704f4762/json/energyUseDataSummaryInfo/1/5/{year_month}'  
    response = requests.get(url)

    if response.status_code == 200:
        print("api 호출 성공")
        # print(response.json())
    else:
        print(f"API 호출 실패: {response.status_code}")
        break

    data_json = response.json()
    # json 파일 안에서 실제 데이터가 들어있는 row 하위만 추출
    for idx in range(0, 5):
        result.append(data_json['energyUseDataSummaryInfo']['row'][idx])
    # result.append(response.json())

# 2-1. 수집한 JSON 형태의 데이터를 pandas DataFrame으로 변환하고,
# 데이터의 기본 정보를 출력하는 코드와 실행 결과를 첨부하시오. (4점)
df = pd.DataFrame(result)
# df.to_json('collectedData.json', indent=4, orient='records', force_ascii=False)
# print(df.info())

df_indivisual = df.loc[df['MM_TYPE']=='개인']
df_indivisual.to_json('collectedData_indivisual.json', indent=4, orient='records', force_ascii=False)
print(df_indivisual.info())

# print(df.loc[df['MM_TYPE'] == '개인'])


# 2-2. 연도별, 계절별 분석을 위해 날짜 컬럼을 활용하여 연도(year)와 계절(season) 컬럼을 추가하는 전처리 코드를 작성하고,

# 변환 결과를 확인할 수 있는 출력 결과를 첨부하시오.
# 계절 구분: 봄(3-5월), 여름(6-8월), 가을(9-11월), 겨울(12-2월) (4점)

