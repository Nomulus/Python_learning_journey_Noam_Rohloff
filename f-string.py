def main():
    sentence()
    maths()
    equal_to()

def sentence():
    name = "Alice"
    age = 25
    print(f"My name is {name} and I'm {age} years old.")

def maths():
    price = 49.99
    quantity = 3
    print(f"Total cost: ${price * quantity:.1f}")

def equal_to():
    x = 10
    y = 20
    print(f"{x=}, {y=}")


if __name__ == "__main__":
    main()