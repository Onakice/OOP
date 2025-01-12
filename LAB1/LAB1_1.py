result = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
print(','.join(result), end=',')
# ต้องการให้ ตัวสุดท้าย ลงท้ายด้วย ,