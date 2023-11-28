import sqlite3 

number = input ("Машинанын номери: ")
brand = input ("Маркасы: ")
model = input ("Модели: ")
years = int(input("Чыккан жылы: "))
service_status = input("Абалы: ")
print(f"Машинанын номери:{number}, Маркасы: {brand}, Модели: {model},Чыккан жылы: {years}, Абалы: {service_status}")

connect = sqlite3.connect("cars.db")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars_users( 
               id INTEGER PRIMARY KEY,
               number INTEGER(255),
               brand VARCHAR(255),
               model VARCHAR(255),
               years INTEGER(255),
               service_status VARCHAR(255)
               ) ''')

cursor.execute(f'''INSERT INTO cars_users (number, brand, model, years, service_status) VALUES ('{number}','{brand}','{model}','{years}','{service_status}')''')
connect.commit()


cursor.execute(f""" SELECT * FROM cars_users""")
date = cursor.fetchall()

for jyiyntyk in date:
    print(f'ID:{jyiyntyk[0]}, Машинанын номери:{jyiyntyk[1]}, Маркасы:{jyiyntyk[2]}, Модели:{jyiyntyk[3]}, Жылы:{jyiyntyk[4]}, Абалы:{jyiyntyk[5]}')


connect.close()