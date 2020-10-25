import os, json, xml.etree.ElementTree as ET

def get_words(file):
    if os.path.splitext(file)[1] == ".json":
        with open("newsafr.json", encoding="utf-8") as f:
            json_data = json.load(f)
            items = json_data["rss"]["channel"]["items"]
            b = []
            for x in items:
                b.extend(x["description"].split(" "))
        return [words for words in b
                if len(words) >= 6]

    if os.path.splitext(file)[1] == ".xml":
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse("newsafr.xml", parser)
        root = tree.getroot()
        items = root.findall("channel/item")
        b = []
        for x in items:
            b.extend(x.find("description").text.split(" "))
        return [words for words in b
                if len(words) >= 6]

def get_sorted_(b):
    forr = {}
    for words in b:
        if words in forr.keys():
            forr[words] = forr[words] + 1
        else:
            forr[words] = 1
    b = sorted(list(forr.items()), key=lambda x:-x[1])
    return b

def print_ten(file):
    x = 0
    for words in get_sorted_(get_words(file)):
        while x < 10:
            print(get_sorted_(get_words(file))[x])
            x = x + 1


def main():
    while True:
        print_ten(input("Введите название файла "))

main()
