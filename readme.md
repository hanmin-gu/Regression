Linear Regression(선형회귀)

손실함수

손실함수가 최솟값을 갖도록 최적화 - 경사 하강법



Linear Regression calcualate process

- input data
- learning (손실함수 값 계산)
- 손실함수 값이 최소이면 output 아니면 보정후 다시 1번째 단계

linear regression implementation using python


- 1.슬라이싱 or list comprehension 등을 이용하여 x 와 정답 t를 numpy 데이터형으로 분리
- 2.y= Wx+b : W =numpy.random.rand(), b=numpy.random.rand()
- 3.손실함수 코드 :
def loss_func():
y= numpy.dot(X,W) + b
return (numpy.sum((t-y)*2)) / (len(x))
- 4.학습률 a(보정값) : learning_rate = 1e-3 or 1e-4 or 1e-5
- 5.W,b 보정식 계산 코드 : f= lambda x : loss_func()
for step in range(6000): 6000은 임의 값
W-= learning_rate * numerical_derivative(f,W)
b-= learning_rate*numerical_derivative(f,b)