
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_user_phone(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact change."

def phone_username(name, contacts):
    if name in contacts:
        print(f"Номер телефону для контакту '{name}': {contacts[name]}")
    else:
        print(f"Контакт '{name}' не знайдено.")

def all_users_phone(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_user_phone(args, contacts))
        elif command == "phone":
             if args:
                phone_username(args[0], contacts)
             else:
                print("Please provide a username.")
        elif command == "all":
            print(all_users_phone(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
