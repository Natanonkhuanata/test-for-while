# เเบบฝึกหัดเรื่อง for-while 5-2

num = 1
sum = 0
print("ถ้าไม่มีใครเข้าไปในลิฟต์ให้น้ำหนักเป็น 0")

for num in range(1,7):
    N = float(input(f"น้ำหนักของคนที่: {num}  >>"))
    sum += N
    if sum > 450:
       print("น้ำหนักเกินกำหนด!!!!")
       N1 = float(input(f"น้ำหนักของคนที่: {num} >>"))
    
    
    num += 1

print(sum - N )


