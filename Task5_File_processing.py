def file_processing(file_name):
    with open(file_name) as text:
        text_list = text.read().split()
        word_dict = {word:text_list.count(word) for word in text_list}
        sorted_dict = dict(sorted(word_dict.items(), key=lambda sd: (-sd[1], sd[0])))
        [print(key,':',value) for key, value in sorted_dict.items()]

file_processing("text.txt")