def main():
    words = {"Python", "Programmierung", "Zufall", "Entwicklung", "Algorithmus", "Daten", "hi", "how", "arse", "you"}

    text_without_words_with_s = [word for word in words if len(word) < 5 and "s" not in word.lower()]

    print(text_without_words_with_s)


if __name__ == "__main__":
    main()