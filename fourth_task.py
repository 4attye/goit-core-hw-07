
def parse_input(user_input):
    """
        Функція що парсить введений рядок на команду та аргументи,
        приводить команду до нижнього регістру і видаляє зайві пробіли,
        повертає команду і список аргументів
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):
    """
        Декоратор для обробки помилок, якщо виникає помилка
        ValueError, повертається повідомлення "Введіть ім'я та телефон",
        KeyError, повертається повідомлення "Контакт не знайдено",
        IndexError, повертається повідомлення "Введіть ім'я".
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner


@input_error
def add_contact(args, contacts):
    """
        Функцію "add_contact" що перевіряє,чи передано аргументи,чи існує контак,
        розпаковує аргументи та додає новий контакт у словник якщо контакта не існує
    """
    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return  "The contact already exists"


@input_error
def change_contact(args, contacts):
    """
        Функцію "change_contact" що перевіряємо, чи передано аргументи,
        розпаковує аргументи та якщо контакт існує оновлює номер телефону
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    """
        Функцію "show_phone" що перевіряє, чи передано аргумент,
        отримує ім'я з аргументів,якщо контакт існує повертає номер телефону
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


@input_error
def show_all(contacts):
    """
        Функцію "show_all" що створює рядок для збереження результату,
        перевіряє, чи є контакти в словнику, проходить через всі контакти і додає їх в result
    """
    if not contacts:
        raise KeyError
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
        return result.strip()


def main():
    """
        Головна функція асистент-бота. Ця функція запускає нескінченний цикл,
        який очікує введення користувачем команд для роботи з контактами.
        В залежності від введеної команди, виконуються відповідні дії:
        - "close" або "exit": завершення роботи програми
        - "hello": виводить привітання
        - "add": додає новий контакт
        - "change": змінює існуючий контакт
        - "phone": виводить номер телефону для вказаного контакту
        - "all": виводить всі збережені контакти
        - невідома команда: виводить повідомлення про помилку
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        match command:
            case "close":
                print("Good bye!")
                break
            case "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
