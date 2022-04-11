# เเบบฝึกหัดเรื่อง for-while 5-4


print("-----Pattern A-----")
for i in range(1,2):
    for j in range(1,i+5):
        print(j,' ',end='')
        continue
    print()
    for j in range(1,i + 4):
        print(j,' ',end='')
        continue
    print()
    for j in range(1,i + 3):
        print(j, ' ', end='')
        continue
    print()
    for j in range(1,i + 2):
        print(j, ' ', end='')
        continue
    print()
    for j in range(1,i + 1):
        print(j, ' ', end='')
        break
    print()

print("-------Pattern A2------")
for i in range(1,2):
    for num in range(1,6):
        print(num,'',end='')

    print()
    for num in range(1,5):
        print(num,'',end='')

    print()
    for num in range(1,4):
        print(num,'',end='')

    print()
    for num in range(1,3):
        print(num,'',end='')

    print()
    for num in range(1,2):
        print(num,'',end='')

    print()

       
    
    

print("-----Pattern B-----")
for i in range(1,6):
    for num in range(i+1,0,-1):
        print('',num,end='')
    
    print()
    for num in range(i+2,0,-1):
        print('',num,end='')
    

