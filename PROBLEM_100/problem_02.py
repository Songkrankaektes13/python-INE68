def find_multiples_of_three_and_four(start: int, end: int) -> list:
    if start < end:
        return[]
    return[n for n in range(start, end+1) if n % 3 == 0 or n % 4 == 0]
print(find_multiples_of_three_and_four(10, 50))

# ให้ฟังก์ชันชื่อ find_multiples_of_three_and_four รับพารามิเตอร์ start และ end
# และคืนค่ารายการของจำนวนเต็มที่เป็นตัวคูณของ 3 หรือ 4 ในช่วง [start, end]
# หาก start มากกว่า end ให้คืนค่าเป็นรายการว่าง