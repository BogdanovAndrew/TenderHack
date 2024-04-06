from pymystem3 import Mystem


stemmer = Mystem()

def stem_req(req: str, remove_prep=False) -> str:
    if remove_prep:
        pass
    stemmed = stemmer.lemmatize(req)
    return "".join(stemmed)


print(stem_req("Метлу для уборку"))