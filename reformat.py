import json

words = {
    "translations": []
}

with open("viet-word.txt",) as fd:
    for index, line in enumerate(fd.readlines()):
        if (index % 3) == 0:
            translation = {
                "VN": line.strip("\n"),
                "EN": ""
            }
        elif (index % 3) == 1: 
            translation["EN"] = line.strip("\n")
        elif (index % 3) == 2:
            words["translations"].append(translation)

with open("data/vd_en_words_translations.json", "w", encoding="utf-8") as fd:
    json.dump(words, fd, ensure_ascii=False) 