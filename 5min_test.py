def main():
    raw_users = ["  Alice", "bob", "ALICE", "charles", "  bob  ", "Alice", "David"]
    print(clean_users(raw_users))

def clean_users(raw_users):
    users = []

    for user in raw_users:
        user = user.strip().capitalize()
        users.append(user)

    return set(users)

if  __name__ == "__main__":
    main()

# Aufgabe: 
# Erstelle eine neue Liste, in der jeder Name:
# 1. Keine Leerzeichen am Anfang oder Ende hat.
# 2. Nur der erste Buchstabe groß ist (Proper Case).
# 3. Jeder Name nur genau EINMAL vorkommt.
# 4. Die Liste am Ende alphabetisch sortiert ist.