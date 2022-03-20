# This is a short script written to demonstrate a point in
# "14_ClassesObjects.py".
class AClass:
    x = 3

    def f(self):
        print("Hello World")


if __name__ == "__main__":
    print(AClass.x)
    print(AClass.f)
