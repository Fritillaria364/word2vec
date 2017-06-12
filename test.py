# -*- coding: utf-8 -*-

from gensim.models import word2vec

data1 = word2vec.LineSentence('./tweets-wakati.txt')
model1 = word2vec.Word2Vec(data1, 
                size=200,
                min_count=5,
                window=5,
                hs=1)
model1.save("./tweets.model")

