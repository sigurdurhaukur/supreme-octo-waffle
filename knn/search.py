import numpy as np
import faiss                      # make faiss available
from gensim.models import KeyedVectors

d = 350                           # dimension

# Load pre-trained embeddings from a file
embeddings = KeyedVectors.load(
    './word2vec-isl/IGC_2021_lemmatized__350__13__9__5__0_05__1_vectors.kv')


# xb = embeddings['talva']  # Get numpy vector of a word
# xb = np.array(xb)            # convert to a NumPy array
# xb = xb.reshape(1, -1)       # reshape to (1, d)

# Get numpy vectors for multiple words and concatenate them along the first axis
words = ['talva', 'amma']
xb = np.concatenate([embeddings[w][np.newaxis, :] for w in words], axis=0)

print(xb.shape)  # should output (2, 350)

xq = embeddings['pilla']  # Get numpy vector of a word
xq = np.array(xq)            # convert to a NumPy array
xq = xb.reshape(1, -1)       # reshape to (1, d)

res = faiss.StandardGpuResources()  # use a single GPU

# Using a flat index

index_flat = faiss.IndexFlatL2(d)  # build a flat (CPU) index

# make it a flat GPU index
gpu_index_flat = faiss.index_cpu_to_gpu(res, 0, index_flat)

gpu_index_flat.add(xb)         # add vectors to the index
print(gpu_index_flat.ntotal)

k = 2                          # we want to see 4 nearest neighbors
D, I = gpu_index_flat.search(xq, k)  # actual search
print(I[:5])                   # neighbors of the 5 first queries
print(I[-5:])                  # neighbors of the 5 last queries
