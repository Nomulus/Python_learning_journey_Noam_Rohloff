from collections import Counter

class TextAnalyzer():
    def __init__(self, text):
        words = self.analyze(text)
        self.counter = Counter(words)

    def analyze(self, text):
        text = text.lower()
        words = text.split()
        text_ohne_sonderzeichnen_und_stopwords = []
        for word in words:
            word = word.strip(".,!?;:")
            if word and word not in self.stopwords:
                text_ohne_sonderzeichnen_und_stopwords.append(word)
        self.longest_word = max(text_ohne_sonderzeichnen_und_stopwords, key = len) if text_ohne_sonderzeichnen_und_stopwords else ""
        return text_ohne_sonderzeichnen_und_stopwords
    
    def __str__(self):
        return (self.concatenate_counter())
    
    def concatenate_counter(self):
        zeilen = []
        zeilen.append(f"\n{self.longest_word} ist das längste Wort\n")
        for i , pair in enumerate(self.counter.most_common(10)):
            zeilen.append(f"{i+1}: {pair[0]}: {pair[1]} Wiederholungen")
        return "\n".join(zeilen)
    
    def get_words_by_threshold(self, min_freq):
        return sorted([word for word, count in self.counter.items() if count >= min_freq])

    @property
    def stopwords(self):
        return {'der', 'die', 'das', 'dem', 'den', 'des', 'ein', 'eine', 'einer', 'einem', 'einen', 'eines',
        'und', 'in', 'zu', 'von', 'mit', 'sich', 'auf', 'ist', 'es', 'nicht', 'an', 'für', 'am', 'im',
        'doch', 'jeder', 'jedes', 'einmal', 'erst', 'als'}
        


def main():
    text_analyzer = TextAnalyzer("Das Haus ist groß, und in dem Haus ist es schön! Doch nicht jeder in dem Haus ist glücklich. Das Glück ist ein flüchtiges Gut, besonders in einem Haus, das mit Sorgen gefüllt ist. Ist das Haus erst einmal leer, ist es still.")
    print(text_analyzer.get_words_by_threshold(2))
    print(text_analyzer)
    write_to_file(text_analyzer, "top_words.txt")

def write_to_file(text_analyzer, filename):
    with open(filename, "w") as file:
        file.write(str(text_analyzer))


if __name__ == "__main__":
    main()