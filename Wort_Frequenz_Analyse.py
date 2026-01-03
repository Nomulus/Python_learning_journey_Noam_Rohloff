class TextAnalyzer():
    def __init__(self, text):
        words = self.analyze(text)
    
    def analyze(self, text):
        text = text.lower()
        words = text.split(" ")
        text_ohne_sonderzeichnen_und_stopwords = []
        for word in words:
            for zeichen in self.sonderzeichen:
                if zeichen in word:
                    word = word.replace(zeichen, "")
            
            found_stop = False
            for stop in self.stopwords:
                if stop == word:
                    found_stop = True
                    break
            if not found_stop:
                text_ohne_sonderzeichnen_und_stopwords.append(word)
        print(text_ohne_sonderzeichnen_und_stopwords)

    @property
    def sonderzeichen(self):
        return [".", ",", "!", "?", ";", ":"]
    
    @property
    def stopwords(self):
        return ['der', 'die', 'das', 'dem', 'den', 'des', 'ein', 'eine', 'einer', 'einem', 'einen', 'eines',
        'und', 'in', 'zu', 'von', 'mit', 'sich', 'auf', 'ist', 'es', 'nicht', 'an', 'für', 'am', 'im',
        'doch', 'jeder', 'jedes', 'einmal', 'erst', 'als']
        


def main():
    text_analyzer = TextAnalyzer("Das Haus ist groß, und in dem Haus ist es schön! Doch nicht jeder in dem Haus ist glücklich. Das Glück ist ein flüchtiges Gut, besonders in einem Haus, das mit Sorgen gefüllt ist. Ist das Haus erst einmal leer, ist es still.")

if __name__ == "__main__":
    main()