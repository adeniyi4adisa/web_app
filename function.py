FILEPATH = "todos.txt"
filepath = f"file/{FILEPATH}"


def get_todos(filept=filepath):
    """ fetch todo items"""
    with open(filept, 'r') as file:
        read_file = file.readlines()
        return read_file


def write_todos(todo_arg, filept=filepath):
    """ write todos into a text file"""
    with open(filept, 'w') as file:
        write_todo = file.writelines(todo_arg)
        return write_todo


if __name__ == "main":
    print("Hello")
