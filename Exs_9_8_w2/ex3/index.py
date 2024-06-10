import re

with open('H:\AIO\Weekly_EXs\Exs_9_8_w2\ex3\P1_data.txt', 'r+') as file: 

    P1_str = ''

    # HACK: split word from phrase
    for phrase in file.readlines():
        P1_str += phrase

    # HACK: all words in str
    words_list = re.split('\W+', P1_str)

    words_dict = {key: words_list.count(key) for key in words_list}
