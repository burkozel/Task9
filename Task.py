import json, xml.etree.ElementTree as ET

def get_words_xml():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    items = root.findall("channel/item")
    b = []
    a = []
    for x in items:
        b.extend(x.find("description").text.split(" "))
    for x in b:
        if len(x) > 6:
            a.append(x)
    return a

def get_words_json():
    with open("newsafr.json", encoding="utf-8") as f:
        json_data = json.load(f)
        items = json_data["rss"]["channel"]["items"]
        b = []
        a = []
        for x in items:
            b.extend(x["description"].split(" "))
        for x in b:
            if len(x) > 6:
                a.append(x)
    return a

def get_sorted_(a):
    forr = {}
    for words in a:
        if words in forr.keys():
            forr[words] += 1
        else:
            forr[words] = 1
    a = sorted(list(forr.items()), key=lambda x:-x[1])
    return a[0:10]


def main():
    while True:
        user = input("Введите команду. Нажмите h для справки по командам ")
        if user == "json":
            print(get_sorted_(get_words_json()))
        if user == "xml":
            print(get_sorted_(get_words_xml()))
        if user == "h":
            print("json - десериализация файла через json. xml - десериализация файла через xml.")
main()