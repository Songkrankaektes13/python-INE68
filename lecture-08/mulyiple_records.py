import struct

num_records = int(input("How many records do you want to create? "))
with open("records.bin", "wb") as file:
    for _ in range(num_records):
        id_num = int(input("enter ID: "))
        name = input("Enter Name: ")
        age = int(input("enter age: "))
        gpa = float(input("enter GPA: "))
        data = struct.pack('i20sif', id-name, name.encode(), age, gpa)
        file.write(data)
print(f"{num_records} records have been written to records.bin") 