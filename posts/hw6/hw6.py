'''
챕터 9-2 설문조사 그래프에서 각 성별 95% 신뢰구간 계산후 그리기

norm.ppf() 사용해서 그릴 것. 모분산은 표본 분산을 사용해서 추정

위 아래 수직 막대기로 표시 (아래 그림 참조)
'''


# 패키지 불러오기
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# 데이터 불러오기
# 처음 데이터는 용량이 커서 어느정도 전처리 된 데이터를 불러왔다.
welfare = pd.read_csv("././data/hw6_welfare.csv")

# 수업 시간 때 그렸던 그래프
sex_income = welfare.dropna(subset = "income") \
       .groupby("sex", as_index=False) \
       .agg(mean_income = ("income", "mean"))
sex_income

sns.barplot(data = sex_income, x = "sex", y = "mean_income", hue = "sex")
plt.show()
plt.clf()

### 각 성별 95% 신뢰구간 계산
# 여성-월급 테이블 / 남성-월급 테이블 뽑기
female_income = welfare \
    .dropna(subset = "income") \
    .query('sex == "female"')[["sex", "income"]]

male_income = welfare \
    .dropna(subset = "income") \
    .query('sex == "male"')[["sex", "income"]]

# 평균 구하기
female_x_var = female_income["income"].mean()
male_x_var = male_income["income"].mean()

# 표본분산 구하기
# sum((female_income["income"] - female_income_mean)**2) / (len(female_income)-1)
female_s_2 = female_income["income"].var()
male_s_2 = male_income["income"].var()

# 표준편차 구하기
female_sigma = np.sqrt(female_s_2)
male_sigma = np.sqrt(male_s_2)

# 신뢰구간 95% 구하기
female_025 = norm.ppf(0.025, loc = female_x_var, scale = female_sigma)
female_975 = norm.ppf(0.975, loc = female_x_var, scale = female_sigma)

male_025 = norm.ppf(0.025, loc = male_x_var, scale = male_sigma)
male_975 = norm.ppf(0.975, loc = male_x_var, scale = male_sigma)

# 시각화 하기.
sex_income = welfare.dropna(subset = "income") \
       .groupby("sex", as_index=False) \
       .agg(mean_income = ("income", "mean"))
sex_income
sns.barplot(data = sex_income, x = "sex", y = "mean_income", hue = "sex")

plt.vlines(x = 0, ymin = female_025, ymax = female_975, colors = "green")
plt.vlines(x = 1, ymin = male_025, ymax = male_975, colors = "green")
plt.show()
plt.clf()




