# Import classes from the package
from My_Package import ClassOne, ClassTwo

def main():
    # Create objects
    obj1 = ClassOne("Alice")
    obj2 = ClassTwo(25)

    # Call methods
    print(obj1.greet())
    print(obj2.show_age())

if __name__ == "__main__":
    main()
