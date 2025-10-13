import requests

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
    url = r"http://openapi.seoul.go.kr:8088/58474744486c6f67393777704f4762/json/energyUseDataSummaryInfo/1/5/" + year_month
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        print("api 호출 성공")
        # print(response.json())
    else:
        print(f"API 호출 실패: {response.status_code}")

    result.append(response)

for item in result:
    print(item.json())

