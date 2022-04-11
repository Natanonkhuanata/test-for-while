# เเบบทดสอบเรื่อง for-while 5-3
n =int(input("ตัวเลขที่ต้องการจัดรูปแบบ >>"))
ramain = n
digit = 0

result = ''

while ramain != 0:
    digit = ramain % 1000 
    if result == '':
        result = str(digit)

    else:
        result = str(digit) + ',' + result

    ramain = ramain // 1000

print("ตัวเลขที่จัดรุปเเบบเเล้วคือ: >>", result)