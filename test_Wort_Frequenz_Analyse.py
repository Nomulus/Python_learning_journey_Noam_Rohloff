import pytest
from Wort_Frequenz_Analyse import TextAnalyzer

@pytest.fixture
def standard_text_analyzer():
    text_analyzer = TextAnalyzer("Das Haus ist groß, und in dem Haus ist es schön! Doch nicht jeder in dem Haus ist glücklich. Das Glück ist ein flüchtiges Gut, besonders in einem Haus, das mit Sorgen gefüllt ist. Ist das Haus erst einmal leer, ist es still.")
    return text_analyzer

def test_str(standard_text_analyzer):
    string = standard_text_analyzer.__str__()
    assert "haus" in string
    assert "Wiederholungen" in string
    
def test_analyze_stopword_removal(standard_text_analyzer):
    assert standard_text_analyzer.analyze("Ich will den haben") == ["ich", "will", "haben"]
    assert standard_text_analyzer.analyze("Ich der den dann den haben") == ["ich", "dann", "haben"]

def test_analyze_sonderzeichen_removal(standard_text_analyzer):
    assert standard_text_analyzer.analyze("Ich!!!! will !!jetzt!!!!!") == ["ich", "will", "jetzt"]
    assert standard_text_analyzer.analyze("Ich.,!! will !!jetzt!!!!.") == ["ich", "will", "jetzt"]

def test_analyze_if_no_text_given(standard_text_analyzer):
    assert standard_text_analyzer.analyze("") == []

def test_analyze_raises_error(standard_text_analyzer):
    with pytest.raises(TypeError):
        standard_text_analyzer.analyze()