from collections import Counter
import re

def get_top_words(file_path, output_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    words = re.findall(r'\b\w+\b', text)
    counter = Counter(words)
    most_common = counter.most_common(top_n)

    with open(output_path, 'w', encoding='utf-8') as out_file:
        for word, count in most_common:
            out_file.write(f'{word}-{count}\n')
