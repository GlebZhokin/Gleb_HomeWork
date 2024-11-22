import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from natasha import Segmenter, NewsEmbedding, NewsMorphTagger, Doc
from natasha.morph.vocab import MorphVocab
from collections import Counter
import os

nltk.download('punkt')
nltk.download('stopwords')

# Морфолосинтаксический парсинг из наташи
segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
morph_vocab = MorphVocab()
stop_words = set(stopwords.words('russian'))

# Список предлогов, союзов и местоимений для исключения (они частично повторяют стоп-слова)
exclude_words = set([
    'и', 'в', 'не', 'на', 'с', 'под', 'к', 'до', 'над', 'из', 'перед', 'при', 'за', 'о', 'об', 'обо', 'про', 'для', 'без', 'у', 'от', 'во', 'со', 'что', 'как', 'так', 'но', 'а', 'или', 'чтобы', 'если', 'когда', 'потому', 'что',
    'я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они', 'себя', 'мой', 'твой', 'его', 'её', 'наш', 'ваш', 'их', 'этот', 'тот', 'каждый', 'сам', 'весь', 'все', 'всякий', 'любой', 'некоторый', 'другой', 'самый', 'какой', 'который', 'чей'
])

# Список Сводеша на 207 слов для русского языка (чтобы наверняка)
swadesh_list = [
    'я', 'ты', 'мы', 'вы', 'он', 'она', 'оно', 'они', 'это', 'этот', 'тот', 'здесь', 'там', 'где', 'куда', 'откуда', 'кто', 'что', 'не', 'все', 'много', 'некоторый', 'один', 'два', 'большой', 'длинный', 'широкий', 'толстый', 'тяжелый', 'маленький', 'короткий', 'узкий', 'тонкий', 'женщина', 'мужчина', 'человек', 'ребенок', 'жена', 'муж', 'мать', 'отец', 'животное', 'рыба', 'птица', 'собака', 'вши', 'дерево', 'лес', 'палка', 'семена', 'лист', 'корень', 'кора', 'цветок', 'трава', 'веревка', 'кожа', 'мясо', 'кровь', 'кость', 'жир', 'яйцо', 'рог', 'хвост', 'перо', 'волосы', 'голова', 'ухо', 'глаз', 'нос', 'рот', 'зуб', 'язык', 'ноготь', 'стопа', 'нога', 'колено', 'рука', 'крыло', 'живот', 'сердце', 'печень', 'пить', 'есть', 'кусать', 'сосать', 'плевать', 'рвать', 'видеть', 'слышать', 'знать', 'думать', 'чувствовать', 'бояться', 'спать', 'жить', 'умирать', 'убивать', 'бороться', 'охотиться', 'ударять', 'резать', 'колоть', 'расщеплять', 'тереть', 'копать', 'плавать', 'летать', 'идти', 'приходить', 'лежать', 'сидеть', 'стоять', 'вертеться', 'падать', 'давать', 'держать', 'сжимать', 'течь', 'замерзать', 'светить', 'сушить', 'дуть', 'дышать', 'смеяться', 'плакать', 'говорить', 'сказать', 'петь', 'играть', 'плавать', 'лететь', 'ползать', 'круглый', 'острый', 'тупой', 'мокрый', 'сухой', 'правильный', 'близкий', 'далекий', 'правый', 'левый', 'на', 'в', 'между', 'потому', 'имя'
]

# Лемматизация списка Сводеша
lemmatized_swadesh_list = []
for word in swadesh_list:
    parse = morph_vocab.parse(word)[0]
    lemma = parse.normal_form
    lemmatized_swadesh_list.append(lemma.lower())

# Объединяем списки исключений
exclude_words.update(lemmatized_swadesh_list)

#Функция для обработки текста и его разбиения на токены
def tokenize_text(text):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)

    words = []
    for token in doc.tokens:
        parse = morph_vocab.parse(token.text)[0]
        lemma = parse.normal_form
        if lemma and lemma.lower() not in stop_words and lemma.lower() not in exclude_words and lemma.isalnum():
            words.append(lemma.lower())
    return words

def load_texts_from_directory(directory):
    texts = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                texts[filename] = f.read()
    return texts

def classify_text(new_text_path, base_texts):
    with open(new_text_path, 'r', encoding='utf-8') as f:
        new_text = f.read()

    # Токенизация текстов
    new_text_words = tokenize_text(new_text)
    new_text_counter = Counter(new_text_words)

    base_texts_processed = {filename: tokenize_text(text) for filename, text in base_texts.items()}
    base_texts_counters = {filename: Counter(words) for filename, words in base_texts_processed.items()}

    # Сравнение нового текста с базой данных
    similarity_scores = {}
    for filename, counter in base_texts_counters.items():
        common_words = set(new_text_counter.keys()) & set(counter.keys())
        common_word_count = sum(min(new_text_counter[word], counter[word]) for word in common_words)
        similarity_scores[filename] = common_word_count / len(new_text_words)

    # Определение темы
    best_match = max(similarity_scores, key=similarity_scores.get)
    return best_match

# Пути к необходимым материалам и загрузка базы данных
base_directory = 'C:/Users/jocki/Desktop/Piton/baza'
base_texts = load_texts_from_directory(base_directory)
new_text_path = 'C:/Users/jocki/Desktop/testing/Новости.txt'

# Результат
best_match = classify_text(new_text_path, base_texts)
print(f"Тема вашего текста - {best_match}")