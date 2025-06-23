from booking import book_cabinet

if __name__ == "__main__":
    cabinet = int(input("Номер кабинета: "))
    name = input("Ваше имя: ")
    email = input("Email: ")
    phone = input("Телефон: ")
    start = input("Начало (YYYY-MM-DD HH:MM): ")
    end = input("Конец (YYYY-MM-DD HH:MM): ")

    print(book_cabinet(cabinet, name, email, phone, start, end))
