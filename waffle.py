
# install dependencies
# ! pip install faiss-cpu
# ! pip install gensim


# download word2vec model (2.5GB)

# ! curl --remote-name-all https://repository.clarin.is/repository/xmlui/bitstream/handle/20.500.12537/209{/word2vec_models.zip}
# ! unzip /work/word2vec_models.zip
# ! unzip -j /work/word2vec_models.zip '*READ*'


import faiss
import numpy as np
from gensim.models import KeyedVectors
vectors = KeyedVectors.load(
    './word2vec-isl/IGC_2021_lemmatized__350__13__9__5__0_05__1_vectors.kv')

xb = vectors.get_normed_vectors()
xb.shape


xq = vectors.get_vector('fiskur', norm=True)
xq = np.reshape(xq, (1, -1)).astype('float32')

xq.shape


nlist = 128  # number of cells/clusters to partition data into
d = 350
k = 4

quantizer = faiss.IndexFlatIP(d)  # how the vectors will be stored/compared
index = faiss.IndexIVFFlat(quantizer, d, nlist)


index.train(xb)  # we must train the index to cluster into cells

# total words: 969714
# last stable at: 484857 or 0.5*969714
percent_of_total = 1*969_714

index.add(xb[:percent_of_total])


index.nprobe = 8  # set how many of nearest cells to search
D, I = index.search(xq, k)


# display results

for i in range(len(I[0])):
    distance = D[0][i]  # small means most relevant
    word_index = I[0][i]
    try:
        results = vectors.most_similar(positive=[vectors[word_index]], topn=1)
        result_word = results[0][0]
        print(f"result: {result_word} \ndistance: {distance} \n")
    except:
        print("something went wrong")
