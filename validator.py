import requests


def correct_req(req: str) -> str:
    resp = requests.get(f"https://speller.yandex.net/services/spellservice.json/checkText?text={req}")
    correct = " ".join(word['s'][0] for word in resp.json())
    
    return correct


print(correct_req("Валек молярный срукояткой"))