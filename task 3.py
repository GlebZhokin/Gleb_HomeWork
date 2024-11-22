import conllu

def find_sentences_with_tags(file_path, tags):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    sentences = conllu.parse(data)
    found = False

    for sentence in sentences:
        sentence_text = ' '.join(token['form'] for token in sentence)
        for token in sentence:
            found_tag = None
            if 'misc' in token and token['misc'] is not None:
                for tag in tags:
                    if any(tag in value for value in token['misc'].values()):
                        found_tag = tag
                        break
            elif 'deprel' in token:
                for tag in tags:
                    if tag in token['deprel']:
                        found_tag = tag
                        break

            if found_tag:
                found = True
                print(f"Предложение: {sentence_text}")
                print(f"Слово: {token['form']}")
                print(f"Тег: {found_tag}")
                print()

    if not found:
        print("Ничего не найдено.")


file_path = 'C:/Users/jocki/Desktop/testing/GramEval2020-Taiga-social-train.conllu'
tags = ['dislocated', 'discourse']
find_sentences_with_tags(file_path, tags)