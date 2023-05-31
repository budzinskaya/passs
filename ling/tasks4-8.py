#task 4

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

#task 5

! pip install spacy_udpipe
! pip install spacy-conll 
import spacy_udpipe
import spacy_conll
spacy_udpipe.download('ru')
spacy_udpipe.download('de')

def make_ud(langcode, text):
  nlp = spacy_udpipe.load(langcode)
  nlp.max_length = 1500000
  nlp.add_pipe("conll_formatter", last=True)

  doc = nlp(text)
  with open(f"{langcode}.conllu", 'w') as f:
    f.write(doc._.conll_str)
  
  #  буду потом использовать
  return doc._.conll_pd

nlp = spacy_udpipe.load('ru')
nlp.max_length = 1500000 # random large number above the limit
nlp.add_pipe("conll_formatter", last=True)

# текст большой, поэтому 5 минут занимает
doc = nlp(text_ru)

doc_de = make_ud('de',text_de)
doc_ru = make_ud('ru',text_ru)

#task 6
import pandas
def pos_stats(df):

  counts = df['UPOS'].value_counts()
  stats = pandas.DataFrame()
  stats.index = counts.index
  stats['count'] = counts.values
  stats['percent'] = stats['count']/stats['count'].sum() * 100

  return stats
pos_stats(doc_de)
pos_stats(doc_ru)

#task 7

def form_vs_lemma_stats(df):
  # словоформы могут иметь заглавные буквы, но решила не заменять исходные
  df['FORM_lower'] = df['FORM'].apply(lambda x: x.lower())
  
  diff_from_lemmas = df[df['FORM_lower'] != df['LEMMA']]
  dfl_counts = diff_from_lemmas[diff_from_lemmas['UPOS'] !='PUNCT']['UPOS'].value_counts()

  stats = pandas.DataFrame()
  stats.index = dfl_counts.index
  stats['count'] = dfl_counts.values
  stats['total'] = ''

  for pos in stats.index:
    total = df['UPOS'].value_counts()[pos]
    stats.at[pos,'total'] = total

  stats['percent'] = stats['count']/stats['total'] * 100
  
  return stats[['count','percent']]

form_vs_lemma_stats(ru_data)

#task 8 
from statistics import median
def sent_medium(text):
  sents = sent_tokenize(text)
  sent_lengths = [len(word_tokenize(sent)) for sent in sents]
  return median(sent_lengths)

''' если первое - читинг
def find_median(sent_lengths):
  count = len(sent_lengths)
  if count % 2 == 1:
    return sorted(sent_lengths)[count//2]
  else:
    return (sorted(sent_lengths)[count//2] + sorted(sent_lengths)[count//2 - 1]) /2
'''

sent_medium(text_de)
sent_medium(text_ru)
