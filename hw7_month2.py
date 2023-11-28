# Задача: Создайте класс Book, представляющий информацию о книгах. У этого класса должны быть следующие атрибуты: title (название книги), author (автор книги) и year (год издания).  
  
# Создайте базу данных для хранения информации о книгах. Создайте таблицу Books с полями id (целое число, первичный ключ), title (строка, название книги), author (строка, автор книги) и year (целое число, год издания).  
  
# Добавьте несколько записей в таблицу Books, представляющих различные книги.  
  
# Далее, реализуйте методы класса Book:  
# - Метод display_info, который выводит информацию о книге в формате "Книга: [название], Автор: [автор], Год: [год]".  
  
# Дополнительное задание:  
# Напишите программу, которая будет взаимодействовать с базой данных и позволит пользователю:  
# - Просматривать информацию о книгах.  
# - Добавлять новые книги с указанием названия, автора и года издания.  
# - Обновлять информацию о существующих книгах (изменять автора или год издания).  
# - Удалять книги по их названию.  
  
# Примечание: Для выполнения этой задачи потребуется работающая система управления базами данных (например, SQLite) и библиотека для работы с ней (например, sqlite3 в Python). 
 
import sqlite3 
 
connect = sqlite3.connect("Library.db") 
cursor = connect.cursor() 
cursor.execute('''CREATE TABLE IF NOT EXISTS books( 
               id INTEGER PRIMARY KEY, 
               title VARCHAR (255), 
               author VARCHAR (255), 
               year INTEGER (4) 
                ) ''') 
 
class Book: 
    def __init__(self): 
        self.title = None 
        self.author = None 
        self.year = None  
 
    def append(self, title, author, year): 
        self.title = title 
        self.author = author 
        self.year = year 
        cursor.execute(f'''INSERT INTO books (title,  author, year) VALUES (?, ?, ?);''', 
                       (title, author, year)) 
        connect.commit() 
 
    def update(self, id): 
        self.title  = input("Введите новое название книги: ") 
        self.author = input("Введите нового автора книги: ") 
        self.year = int(input("Введите новый год издания книги: ")) 
        cursor.execute(f'''UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?;''', 
                       (self.title, self.author, self.year, id)) 
        connect.commit() 
 
    def delete(self, id): 
        cursor.execute(f"DELETE FROM books WHERE id = ?;", (id,)) 
        connect.commit() 
 
    def display_info(self): 
        cursor.execute('SELECT * FROM books;') 
        date = cursor.fetchall()
        for result in date:
            print (f"Книга: {result[1]}, Автор: {result[2]}, Год: {result[3]};" )
        
 
    def main(self): 
        while True: 
            print("Выберите действие: ") 
            tandoo = int(input("1-Добавить книгу, 2- Обновить книгу 3-Удалить, 0-выйти \n→:")) 
            if tandoo == 0: 
                print("Всего доброго!") 
                break 
            elif tandoo == 1: 
                title = input("Введите имя книга: ") 
                author = input("Введите имя Автора: ") 
                year = int(input("Введите год издание книга: ")) 
                self.append(title, author, year) 
            elif tandoo == 2: 
                id = int(input("Выберите id, чтобы обновить книгу ")) 
                self.update(id) 
            elif tandoo == 3: 
                for_delete = int(input("Напишите id, чтобы удалить книгу: ")) 
                self.delete(for_delete) 
            else: 
                print("Нет такого выбора! Пожалуйста, попробуйте еще раз.") 
 
library = Book() 
library.display_info() 
library.main()