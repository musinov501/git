# n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi dastur tuzilsin. S=1.1-1.2+1.3-...
#(n ta qo'shiluvchi, ishoralar almashib keladi. Shart operatoridan foydalanmang)   
#1-misol


n=int(input("n sonini kiriting: "))

S=0
i=1.1
ishora=1

while i <= 1 + 0.1 * n:
    S += ishora * i
    ishora *= -1
    i += 0.1

print("Yigindi: ", S)    



