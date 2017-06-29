import collections
import json

import chardet

json_files = ['newscy.json', 'newsfr.json', 'newsafr.json', 'newsit.json', ]


def get_top_words(json_file, num_of_word):
    with open(json_file, 'rb') as f:
        data = f.read()
        text = data.decode(chardet.detect(data)['encoding'])
    json_data = json.loads(text)
    news_list = list(
        map(lambda x: x['title'] + ' ' + x['description'], [i for i in json_data['rss']['channel']['items']]))
    news_str = ''.join(news_list)
    news_list = news_str.split(" ")
    news_list = [i for i in news_list if len(i) > 6]
    news_collect = collections.Counter()
    for i in news_list:
        news_collect[i] += 1
    top_words = news_collect.most_common(num_of_word)
    return list(map(lambda x: x[0], [i for i in top_words]))


if __name__ == '__main__':
    for i in json_files:
        print('Введите топ из скольки слов вы хотите видеть для файла {}:'.format(i))
        word_quantity = input()
        top_word_list = get_top_words(i, int(word_quantity))
        print('Для файла {} top 10: \n {} \n'.format(i, top_word_list))
