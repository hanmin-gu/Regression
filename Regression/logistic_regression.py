#수치미분
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


x_data=np.array([1,4,2,1,5,6,7,3,1,1]).reshape(10,1)
t_data=np.array([1,3,7,1,1,9,1,1,1,1]).reshape(10,1)


W=np.random.rand(1,1)
b=np.random.rand(1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def loss_func(x,t):

    delta = 1e-7

    z=np.dot(x,W) + b
    y=sigmoid(z)

    return -np.sum(t*np.log(y+delta) + (1-t)*np.log((1-y)+delta))

def error_val(x,t):
    delta=1e-7

    z=np.dot(x,W) +b
    y= sigmoid(z)
    return -np.sum(t*np.log(y+delta) + (1-t)*np.log((1-y)+delta))

def predict(x):

    z=np.dot(x,W) + b
    y= sigmoid(z)

    if y > 0.5:
        result =1
    else:
        result =0

    return y,result

learning_rate=1e-2

f=lambda x: loss_func(x_data,t_data)

for step in range(10001):
    W-= learning_rate *  numerical_derivative2(f,W)
    b-= learning_rate * numerical_derivative2(f,b)

    if(step % 400 ==0):
        print("step = ",step, "error value = " , error_val(x_data,t_data), "W =", W , "b = ",b)

(r_value, l_value)=predict(13)
