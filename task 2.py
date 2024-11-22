import spacy
nlp = spacy.load("ru_core_news_sm")

with open('C:/Users/jocki/Desktop/testing/Новости.txt', 'r', encoding='utf-8') as file:
    text = file.read()

doc = nlp(text)

# Извлечение именованных сущностей
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Разбивка по категориям
categories = {}
for entity, label in entities:
    if label not in categories:
        categories[label] = []
    categories[label].append(entity)

# Результат
for label, entities in categories.items():
    print(f"{label}: {', '.join(entities)}")