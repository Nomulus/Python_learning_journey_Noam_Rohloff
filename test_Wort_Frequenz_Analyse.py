import pytest
from Wort_Frequenz_Analyse import TextAnalyzer

@pytest.fixture
def standard_text_analyzer():
    text_analyzer = TextAnalyzer("Das Haus ist groß, und in dem Haus ist es schön! Doch nicht jeder in dem Haus ist glücklich. Das Glück ist ein flüchtiges Gut, besonders in einem Haus, das mit Sorgen gefüllt ist. Ist das Haus erst einmal leer, ist es still.")
    return text_analyzer

