class WrongInputOrder(Exception):
    pass


class WrongShowInputOrder(Exception):
    pass


class WrongInputNumber(Exception):
    pass


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        text_arguments_list = args[0]
        try:
            if len(text_arguments_list) != 2:
                raise WrongInputNumber
            if text_arguments_list[0].isalpha() is False or text_arguments_list[1].isdigit() is False:
                raise WrongInputOrder
            return func(*args, **kwargs)
        except WrongInputOrder:
            return "Type name first and phone second"
        except WrongInputNumber:
            return f"Wrong number of inputs. 2 is required"
        except:
            return "This is some other error in input_error"

    return inner


def show_error(func):
    def inner(*args, **kwargs):
        text_arguments_list = args[0]
        try:
            if len(text_arguments_list) != 1:
                raise WrongInputNumber
            if text_arguments_list[0].isalpha() is False:
                raise WrongShowInputOrder
            return func(*args, **kwargs)
        except WrongShowInputOrder:
            return "Type name after the 'phone' command"
        except WrongInputNumber:
            return f"Wrong number of inputs. 1 is required"
        except:
            return "This is some other error in show_error"

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact is added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact is updated"
    else:
        return "Contact is not found"


@show_error
def show_contact(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return str(contacts[name])
    else:
        return "Contact is not found"


def show_all_contacts(contacts):
    users = ''
    for username, phone in contacts.items():
        users += f"{username} {phone}\n"
    return users


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts), end='')
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
