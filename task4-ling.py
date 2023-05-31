!pip install nltk
import nltk
nltk.download('punkt')

def preprocess_text(filepath, regex):
    with open(filepath, 'r') as file:
        text = file.read()
        text = re.sub(regex, '', text)
        text = re.sub(r'\s+', ' ', text)
        
        return text
from tabulate import tabulate
from nltk.tokenize import sent_tokenize, word_tokenize

def analyze_text(text, word_regex):
    sents = sent_tokenize(text)
    tokens = word_tokenize(text)

    reg = re.compile(word_regex)
    words = [token for token in tokens if re.fullmatch(reg, token)]

    sent_lengths = [len(word_tokenize(sent)) for sent in sents]
    mean_length = sum(sent_lengths) / len(sent_lengths)

    results = {
        'кол-во предложений': len(sents),
        'кол-во токенов': len(tokens),
        'средняя длина предложения': mean_length,
        'уникальные токены/все токены': len(set(tokens)) / len(tokens),
        'знаки пунктуации/слова': (len(tokens) - len(words)) / len(words)
    }

    return results


text_ru = preprocess_text('prestuplenie-i-nakazanie.txt', r'[^А-Яа-яЁё.,:;!?–—\-()"\s]+')
text_de = preprocess_text('verbrechen_und_strafe.txt', r'[^A-Za-zÄäÖöÜüß.,:;!?–—\-()"\s]+')

analysis_ru = analyze_text(text_ru, r'[А-Яа-яЁё\-]+')
analysis_de = analyze_text(text_de, r'[A-Za-zÄäÖöÜüß]+')

table_data = [
    ['', 'ru', 'de', 'ru/de'],
]

for key in analysis_ru.keys():
    table_data.append([key, analysis_ru[key], analysis_de[key], analysis_ru[key] / analysis_de[key]])

print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
