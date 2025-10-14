import pandas as pd

df = pd.read_json('collectedData.json', orient='records')
print(df.info())
print(df)
data = list()
# 2-2. 연도별, 계절별 분석을 위해 날짜 컬럼을 활용하여 연도(year)와 계절(season) 컬럼을 추가하는 전처리 코드를 작성하고,
for idx in range(0, 120):
    data.append(df["energyUseDataSummaryInfo"][idx]["row"])
print(data)
df = pd.DataFrame(data)
renamed_df = df.rename(columns={0: '공공주택관리소', 1:'기업', 2:'개인', 3:'공공기관', 4:'학교'})
print(renamed_df)
# print(df[0][0])

# 변환 결과를 확인할 수 있는 출력 결과를 첨부하시오.
# 계절 구분: 봄(3-5월), 여름(6-8월), 가을(9-11월), 겨울(12-2월) (4점)
# data = df.loc['energyUseDataSummaryInfo']['0']
# print(data)


# 문제 3. 데이터 시각화 (8점)
# 전처리된 데이터를 활용하여 다음의 시각화를 수행하시오.
# 3-1. 연도별 에너지 사용 총 사용량(전기+가스+수도+지역난방) 변화량을 선 그래프로 시각화하고,
# 그래프에 자신의 학번 뒤 4자리를 제목에 포함하여 저장하시오. (예: "연도별 에너지 사용 총액 변
# 화 - 1234") 시각화 코드와 생성된 그래프를 첨부하시오. (4점)
# 3-2. 계절별 가스 사용량 평균을 막대 그래프로 시각화하고, 각 막대에 구체적인 수치를 표시하시
# 오. 시각화 코드와 생성된 그래프를 첨부하시오. (4점)
# 문제 4. 데이터 분석 및 해석 (4점)
# 시각화 결과를 바탕으로 다음을 분석하고 설명하시오.
# 4. 연도별 에너지 사용량 변화에서 나타나는 주요 트렌드를 찾아 분석하고, 그 원인을 추론하여
# 200자 이내로 설명하시오. (4점)