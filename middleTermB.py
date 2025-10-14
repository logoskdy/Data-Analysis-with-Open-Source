import requests
import pandas as pd

# 1-2. Python을 사용하여 API를 호출하는 코드를 작성하고,
# 2015년 1월부터 2024년 12월까지의 개인 유형의 현년 전기, 가스, 수도, 지역난방 에너지 사용량 데이터를 수집하는 프로그램을 작성하시오.
# API 호출 성공을 확인할 수 있는 실행 결과를 캡처하여 첨부하시오. (7점)
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
    url = "http://openapi.seoul.go.kr:8088/58474744486c6f67393777704f4762/json/energyUseDataSummaryInfo/1/5/" + year_month
    response = requests.get(url)
    # 아래 jso으로 저장하는 과정에서 원 자료에서 인코딩 문제가 발생함.
    # 이를 해결하기 위해 response 객체에서 인코딩 방식을 강제 지정.
    # response.encoding = 'utf-8'

    if response.status_code == 200:
        print("api 호출 성공")
        # print(response.json())
    else:
        print(f"API 호출 실패: {response.status_code}")

    result.append(response.json())

# 2-1. 수집한 JSON 형태의 데이터를 pandas DataFrame으로 변환하고,
# 데이터의 기본 정보를 출력하는 코드와 실행 결과를 첨부하시오. (4점)
df = pd.DataFrame(result)
print(df.info())
# print(df.describe())

for item in df.values.tolist():
    print(item)

df.to_json('collectedData.json', indent=4, force_ascii=False)


# 2-2. 연도별, 계절별 분석을 위해 날짜 컬럼을 활용하여 연도(year)와 계절(season) 컬럼을 추가하는 전처리 코드를 작성하고,

# 변환 결과를 확인할 수 있는 출력 결과를 첨부하시오.
# 계절 구분: 봄(3-5월), 여름(6-8월), 가을(9-11월), 겨울(12-2월) (4점)

