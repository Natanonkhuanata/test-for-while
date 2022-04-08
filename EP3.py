# เเบบฝึกหัดเรื่อง for-while

number = int(input("Your number you like >>>"))
max = 0
w = ''
sum = 0
while  w != 0:
    w = number % 10
    if max < w:
        max = w
    elif max == w:
        max = w
    
    number = number // 10
    sum += w


print("ตัวเลขที่มีค่ามากที่สุด :" , max)
print("ผลบวกของเลขโดดทั้งหมด :", sum)