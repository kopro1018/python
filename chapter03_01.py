#데이터타입
str1 = "Python"
bool1 = True
str2 = "Anaconda"
float_v = 10.0 # 10 == 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine learning",
    "version": 2.0
}

tuple = (7, 8, 9)
set = {3, 5, 7}

print(type(str1))
print(type(bool1))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))


# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x**y, 2**3 = 8 , pow(2, 3)
"""

# 정수
i=77
i2=-14
big_int=7777777777777777777777777777777777777777777777

print(i)
print(i2)
print(big_int)
 
# 실수
f=0.9999
f2=3.141592
f3=-3.1
f4=3/9

print(f)
print(f2)
print(f3)
print(f4)


#연산해보기
i1=39
i2=939
big_int1=11111111111111111111111111111111111
big_int2=22222222222222222222222222222222222
f1=1.234
f2=3.111

print(">>>>>>+")
print("i1+i2 : ", i1+i2)
print("f1+f2 : ", f1+f2)
print("big_int1+big_int2 : ", big_int1+big_int2)

#서로 다른 타입을 연산하면 형변환이 자동으로 이뤄짐.
print("i1+f2 : ", i1+f2)

# 형 변환
a=3. #0생략가능
b=6
c=.7 #0생략가능
d=12.7

#타입출력
print(type(a), type(b), type(c), type(d))


#형변환2
print(float(b))
print(int(c))
print(int(d))
print(int(True))  # true:1 , false:0
print(float(False))
print(complex(3))
print(complex('3')) # 문자형 > 숫자형
print(complex(False))


#수치 연산 함수
print(abs(-7))

x, y = divmod(100,8)
print(x,y)
print(pow(5,3), 5**3)



#외부모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi) #원주율


