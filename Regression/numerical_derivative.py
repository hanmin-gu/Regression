import numpy as np
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

