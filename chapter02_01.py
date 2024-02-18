# Chpater02-1
# 파이썬 완전 기초

# 기본출력
print('Python start!')
print("Python start!")
#print('''Python start!''') 잘안써~
#print("""Python start!""") 잘안써~

#개행
print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='') #문자 사이에 들어갈 내용, 출력값:PYTHON
print('010', '0000', '3549', sep='-') #문자 사이에 들어갈 내용, 출력값:010-0000-3549
print()


# end 옵션
# 개행없이 한줄로 출력하기, 출력값 : Welcome to IT NEWS Web Site
print('Welcome to', end=' ')
print('IT NEWS', end=' ')
print('Web Site')


# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()


# format 사용(d:3, s:python, f:3.14)
print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', '2'))
print('{0} {1}' .format('one', 'two'))
print('{1} {0}' .format('one', 'two'))
print('%s %s' % ('one', '2'))
print('%d %s' % (1, '2'))
print()



#%S 문자
print('%10s' % ('nice')) #왼쪽5개 공간 확보
print('{:>10}' .format('nice')) #왼쪽5개 공간 확보


print('%-10s' % ('nice')) #오른쪽5개 공간 확보
print('{:10}' .format('nice')) #오른쪽5개 공간 확보

print('{:_>10}' .format('nice')) #밑줄포함 10
print('{:^10}' .format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) #5글자만출력
print('{:10.5}' .format('pythonstudy')) #5글자만출력하지만 공간은 10개를 갖고있음!


# %d 정수
print('%4d' % (12))
print('{:4d}' .format(12))

# %f 소수
print('%f' % (3.14141414141414))
print('{:f}' .format(3.14141414141414))
print('%06.2f' % (3.14141414141414)) #6개 자리 중 정수는 1개여서 0으로 채우고 나머지 2개를 출력함.
print('{:06.2f}' .format(3.14141414141414)) #6개 자리 중 정수는 1개여서 0으로 채우고 나머지 2개를 출력함.


# Chapter02-1-ex1(확장판)
# 참조 : https://realpython.com/python-f-strings/
# 파이썬 3가지 Print Formatting

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'


# 출력1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y)) # %d
print(ex1)


# 출력2
ex2 = 'n = {n}, s = {serialno}, sum={sum}'.format(n=n, serialno=text, sum=x + y)
print(ex2)


# 출력3
ex3 = f'n = {n}, s = {text}, sum={x + y}'
print(ex3)

# 출력4(다양한 f-string 연습)
print(f'n = {n}, s = {text}, sum={x + y}')
print()

# 진수
# (2진수 : b, 8진수 : o, 16진수 : x|X)
k = 98

print(f"k 2진수: {k:b}, k 8진수: {k:o}")
print(f"k 16진수 - l:{k:x}, U:{k:X}")

print()
print()


# 구분기호
m = 10000000000

print(f"m: {m:,}")

print()
print()


# 정렬
# ^ : 가운데 , < : 왼쪽 , > : 오른쪽
t = 20

print(f"t :{t:10}")
print(f"t center: {t:^10}")
print(f"t left: {t:<10}")
print(f"t right: {t:>10}")

print()
print()


# 빈칸 채우기
print(f"t:{t:-^10}")
print(f"t:{t:#<10}")