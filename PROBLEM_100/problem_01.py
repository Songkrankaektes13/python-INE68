def find_mulipes_of_three(start: int, end: int) -> list:

    if start > end:
        return[]
    return [n for n in range(start, end+1) if n % 3 == 0]
print(find_mulipes_of_three(10, 25))

# ให้ฟังก์ชันชื่อ find_multiples_of_three รับพารามิเตอร์ start และ end
# และคืนค่ารายการของจำนวนเต็มที่เป็นตัวคูณของ 3 ในช่วง [start, end]
# หาก start มากกว่า end ให้คืนค่าเป็นรายการว่าง
