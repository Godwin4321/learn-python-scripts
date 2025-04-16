print("This is file1.py")
print(__name__)


def greet():
    print("Hello from file1!")


if __name__ == "__main__":
    print("Running file1 directly!")
    greet()
