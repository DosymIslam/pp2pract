print('abc'.upper()) #ABC

print(2+3*2) #8

print ([1,2,3][1:]) #[2,3]

s=0
for i in range(3):
    s+=1
print(s)

#3

x=5
print('A' if x>3 else 'B')

#A

def f():
    return 7
print(f())

#7

d={'a':1}
print(d.get('b'))
#None

print (sum([1,2,3])) #1 + 2 + 3 = 6 

class A:
    x=5
print(A().x) #5

print(bool([])) #false