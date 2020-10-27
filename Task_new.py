import os, json, xml.etree.ElementTree as ET

def get_words(file, letters_number):
    not_sorted_list = []

    if os.path.splitext(file)[1] == ".json":
        with open(file, encoding="utf-8") as f:
            json_data = json.load(f)
            items = json_data["rss"]["channel"]["items"]
            for x in items:
                not_sorted_list.extend(x["description"].split(" "))

    if os.path.splitext(file)[1] == ".xml":
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse("newsafr.xml", parser)
        root = tree.getroot()
        items = root.findall("channel/item")
        for x in items:
            not_sorted_list.extend(x.find("description").text.split(" "))

    return [words for words in not_sorted_list if len(words) >= letters_number]

def get_sorted_(not_sorted_list):
    count_words = {}
    for word in not_sorted_list:
        if word in count_words.keys():
            count_words[word] = count_words[word] + 1
        else:
            count_words[word] = 1
    sorted_list = sorted(list(count_words.items()), key=lambda x:-x[1])
    return sorted_list

def print_some_words(file, words_number, letters_number):
    print(get_sorted_(get_words(file, letters_number))[:words_number])

def main():
    while True:
        print_some_words(input("Введите название файла "), int(input("Введите количество слов для отображения ")), int(input("Введите минимальную длину слова ")))
main()
