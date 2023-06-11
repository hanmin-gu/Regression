import pandas as pd
import requests
import matplotlib.pyplot as plt

import numpy as np

from tqdm import tqdm


def get_Lotto_Win_Info(start_Round, end_Round):

    drwt_No1 = []

    drwt_No2 = []

    drwt_No3 = []

    drwt_No4 = []

    drwt_No5 = []

    drwt_No6 = []

    bnus_No = []

    for i in tqdm(range(start_Round, end_Round+1, 1)):

        # i = 1

        req_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(i)

        req_lotto = requests.get(req_url)

        lotto_No = req_lotto.json()

        drwt_No1.append(lotto_No['drwtNo1'])

        drwt_No2.append(lotto_No['drwtNo2'])

        drwt_No3.append(lotto_No['drwtNo3'])

        drwt_No4.append(lotto_No['drwtNo4'])

        drwt_No5.append(lotto_No['drwtNo5'])

        drwt_No6.append(lotto_No['drwtNo6'])

        bnus_No.append(lotto_No['bnusNo'])

        lotto_dict = {"Num1":drwt_No1, "Num2":drwt_No2,"Num3":drwt_No3, "Num4":drwt_No4, "Num5":drwt_No5, "Num6":drwt_No6, "bnsNum":bnus_No  }

        lotto_df = pd.DataFrame(lotto_dict)

    return lotto_df

start_Round = 1
end_Round = 100
##lotto_df = get_Lotto_Win_Info(start_Round, end_Round)

##print(lotto_df)

##lotto_df.to_csv(str(start_Round) + '-' + str(end_Round) + '_lotto_number.csv', index = False, encoding = 'utf-8-sig')

x=np.arange(1,6)
y=1.5*x+1.8
plt.plot(x,y)#옵션
plt.show()
x__data=[x for x in [1,2,3,4,5]]
y__data=[y for y in [3,5,7,8,9]]
plt.grid()
plt.scatter(x__data, y__data, color= 'b',marker='o' )#옵션
plt.show()


"""
x_data = np.random.rand(100)
y_data = np.random.rand(100)
plt.title('test')
plt.grid()#격자
plt.scatter(x_data, y_data, color= 'b',marker='o' )#옵션
plt.show()

x__data=[x for x in range(-10,10)]
y__data=[y for y in range(-10,10)]
plt.grid()
plt.plot(x__data, y__data, color= 'b' )#옵션
plt.show()
"""
def solution(s):
    for i in range(len(s) // 2):
        j = len(s) -1 - i
        if s[i] != s[j]:
            return -1
        return 1

print(solution("abcd"))
print(solution("abba"))
print(solution("a"))




