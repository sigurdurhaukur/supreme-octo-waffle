
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
    '/work/IGC_2021_lemmatized__350__13__9__5__0_05__1_vectors.kv')

xb = vectors.get_normed_vectors()
xb.shape


xq = vectors.get_vector('reiður', norm=True)
xq = np.reshape(xq, (1, -1)).astype('float32')

xq.shape


nlist = 128  # number of cells/clusters to partition data into
d = 350
k = 4

quantizer = faiss.IndexFlatIP(d)  # how the vectors will be stored/compared
index = faiss.IndexIVFFlat(quantizer, d, nlist)


index.train(xb)  # we must train the index to cluster into cells

# total words: 969714
# stable at: 484857 or 969714 / 2
index.add(xb[:484857])


index.nprobe = 8  # set how many of nearest cells to search
D, I = index.search(xq, k)


# display results
for _ in I:
    for i in _:
        if i > 0:
            results = vectors.most_similar(positive=[vectors[i]], topn=1)
            result_word = results[0]
            print(result_word)
