fName = "todo.txt"


def get_todo(filename=fName):
    with open(filename, "r") as file1:
        todos1 = file1.readlines()
    return todos1


def write_todo(todo_element, filename="todo.txt"):
    with open(fName, "w") as file1:
        file1.writelines(todo_element)


if __name__ == "__main__":
    print(__name__)
    print(type(__name__))
    print("hello")
    print(get_todo())
