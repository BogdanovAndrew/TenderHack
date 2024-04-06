from pymystem3 import Mystem
# from gensim.models import FastText


stemmer = Mystem()

def stem_req(req: str, remove_prep=False) -> str:
    if remove_prep:
        pass
    stemmed = stemmer.lemmatize(req)
    return "".join(stemmed)


# ft = FastText()
