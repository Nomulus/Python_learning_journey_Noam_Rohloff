def main() -> None:
    lezz_try = infinite_generator
    
def infinite_generator():
    number = 0
    while True:
        print(number)
        yield number
        number += 1