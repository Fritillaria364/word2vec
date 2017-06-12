# -*- coding: utf-8 -*-

from gensim.models import word2vec
import nltk
import sys
import re

# ----------------------------------

twt = open("tweets-hinsi.txt", "r")

raw = []
dic = {}
for line in twt:
    raw.append(re.sub("\t|\n",",",line).split(","))

for raw_list in raw:
    # print(raw_list)
    if not (raw_list[0] == "EOS"
            or re.match("[。、…「」]|\u3000", raw_list[0])
            or raw_list[7] == "ない")\
            and raw_list[1] == "形容詞":
        # print("surface:"+raw_list[0]+" base:"+raw_list[7]+" pos:"+raw_list[1]+" pos1:"+raw_list[2])
        dic[raw_list[7]] = dic.get(raw_list[7], 0) + 1

dic10Within = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:15]
# ------------------------------------

model = word2vec.Word2Vec.load("./tweets.model")

for freq in dic10Within:
    results = model.most_similar(positive=freq[0], topn=10)
    print("---dist from " + freq[0] + "---")
    for result in results:
        print(result)
    print("--------------")


