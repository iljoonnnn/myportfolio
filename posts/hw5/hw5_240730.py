'''
표본 분산 계산 시 왜 n-1로 나누는지
알아보도록 하겠습니다.

균일분포 (3, 7)에서 20개의 표본을 뽑아서
분산을 2가지 방법으로 추정해보세요.

n-1로 나눈 것을 s_2, n으로 나눈 것을 k_2로 정의하고,
s_2의 분포와 k_2의 분포를 그려주세요! (10000개 사용)

각 분포 그래프에 모분산의 위치에 녹색 막대를 그려주세요.

결과를 살펴보고,
왜 n-1로 나눈 것을 분산을 추정하는 지표로 사용하는 것이 타당한지 써주세요!
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import uniform

# 표본 분산 계산해보기.
np.random.seed(20240729)
x = uniform.rvs(loc = 3, scale = 4, size = 20)
x_bar = np.mean(x)
sum((x - x_bar)**2) / (len(x)-1)
# 1.669

# 이론적인 분산 값
my_var = uniform.var(loc = 3, scale = 4)
# 1.333

# 몬테카를로 시뮬레이션을 이용해서 분산값 구하기.
np.random.seed(20240729)
x = uniform.rvs(loc = 3, scale = 4, size = 20 * 10000)
x.shape
x = np.reshape(x, (-1, 20))
x.shape
s_2 = x.var(axis = 1, ddof = 1)  # n-1 으로 나누기.
k_2 = x.var(axis = 1, ddof = 0) # n 으로 나누기.

# s_2 그래프 그리기
plt.hist(s_2, bins = 40)
plt.axvline(my_var, color = 'green', linestyle = 'dashed', linewidth = 2)
plt.show()
plt.clf()

# k_2 그래프 그리기기
plt.hist(k_2, bins = 40)
plt.axvline(my_var, color = 'green', linestyle = 'dashed', linewidth = 2)
plt.show()
plt.clf()
# k_2가 조금 더 가까운 것으로 확인 된다.

# 이번엔 어떤 것이 이론적인 값에 가까웠는지 각각 경우마다 싸움을 붙여보겠다.
result = []
for i in range(10000):
    if (s_2[i] - my_var)**2 < (k_2[i] - my_var)**2:
        result.append("n-1")
    elif (s_2[i] - my_var)**2 > (k_2[i] - my_var)**2:
        result.append("n")
# 10000개의 분산값을 각각 비교해서 이론적인 분산에 더 가까우면 그 방법을 1점 주는 반복문.

# 싸움 결과 시각화.
sns.countplot(data = result)
plt.show()
plt.clf()
# n-1이 더 효과 있따!!!
