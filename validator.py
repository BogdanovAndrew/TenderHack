import requests


def correct_req(req: str) -> str:
    correct_words = []
    for word in req.split():
        resp = requests.get(f"https://speller.yandex.net/services/spellservice.json/checkText?text={word}").json()
        if resp:
            correct_words.append(resp[0]['s'][0])
        else:
            correct_words.append(word)
    return " ".join(correct_words)




# print(correct_req("Ноутбука Xyaomi"))