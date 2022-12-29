import pandas as pd
import requests

import numpy as np

from tqdm import tqdm

##from test.test1 import dictlist, temp


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

print(np.random.normal(0,1,10).reshape(2,5))



def my_func1(input_obj):
    x=input_obj[0]
    y=input_obj[1]


    return x*np.power(y,2)+x
def my_func2(input_obj):
    x=input_obj[0,0]
    y=input_obj[0,1]
    z=input_obj[1,0]
    w=input_obj[1,1]
    return x*y*z+np.power(z,2)+w**2

def numerical_derivative1(f,x):

    h= 1e-4 #  h값 ; 1e-4 적합한 값
    return (f(x+h) - f(x-h)) / (2*h)





#다변수 편미분
def numerical_derivative2(f,x):
    h=1e-4
    grad=np.zeros_like(x)

    it= np.nditer(x, flags=['multi_index'],op_flags=['readwrite'])

    while not it.finished:
        idx=it.multi_index

        temp_val=x[idx]
        x[idx]= float(temp_val) + h
        fx1=f(x)

        x[idx]= temp_val - h
        fx2=f(x)
        grad[idx]=(fx1-fx2) / (2*h)

        x[idx]= temp_val
        it.iternext()

    return grad


result1=numerical_derivative2(my_func1,np.array([1.0,2.0]))
result2=numerical_derivative2(my_func2, np.array([[1.0,2.0],[5.0,4.0]]))

##print(result1)
##print(result2)


def my_func1(input_obj):
    x=input_obj[0]
    y=input_obj[1]


    return x*np.power(y,2)+x

def my_func2(input_obj):
    x=input_obj[0,0]
    y=input_obj[0,1]
    z=input_obj[1,0]
    w=input_obj[1,1]
    return x*y*z+np.power(z,2)+w**2

def numerical_derivative1(f,x):

    h= 1e-4 #  h값 ; 1e-4 적합한 값
    return (f(x+h) - f(x-h)) / (2*h)





#다변수 편미분
def numerical_derivative2(f,x):
    h=1e-4
    grad=np.zeros_like(x)

    it= np.nditer(x, flags=['multi_index'],op_flags=['readwrite'])

    while not it.finished:
        idx=it.multi_index

        temp_val=x[idx]
        x[idx]= float(temp_val) + h
        fx1=f(x)

        x[idx]= temp_val - h
        fx2=f(x)
        grad[idx]=(fx1-fx2) / (2*h)

        x[idx]= temp_val
        it.iternext()

    return grad


result1=numerical_derivative2(my_func1,np.array([1.0,2.0]))
result2=numerical_derivative2(my_func2, np.array([[1.0,2.0],[5.0,4.0]]))

import matplotlib.pyplot as plt

x=np.arange(1,6)
y=1.5*x+1.8
##plt.plot(x,y)#옵션
##plt.show()
x__data=[x for x in [1,2,3,4,5]]
y__data=[y for y in [3,5,7,8,9]]
##plt.grid()
##plt.scatter(x__data, y__data, color= 'b',marker='o' )#옵션
##plt.show()

##dictlist.append(temp)
##sorted_dict= sorted(dictlist, key=getKey, reverse=True) # list를 입력 줄 수로 정렬
##print (sorted_dict[:100]) # List의 상위 10객값만 출

test=np.array([[1,2,3,4],[1,2,5,8]]).reshape(8,)
print(test)
