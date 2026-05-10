import os

def main():
    txt_data = "I like pizza!"

    file_path = "output.txt"

    with open(file = file_path, mode ="w") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
    
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print(file_path, "exists")

if __name__ == "__main__":
    main()