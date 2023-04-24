# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import faiss                     # make faiss available
import numpy as np

d = 64                           # dimension
nb = 10                      # database size
nq = 10                       # nb of queries
np.random.seed(1234)             # make reproducible
xb = np.random.random((nb, d)).astype('float32')
xb[:, 0] += np.arange(nb) / 10.
xq = np.random.random((nq, d)).astype('float32')
xq[:, 0] += np.arange(nq) / 10.


res = faiss.StandardGpuResources()  # use a single GPU

# Using a flat index

index_flat = faiss.IndexFlatL2(d)  # build a flat (CPU) index

# make it a flat GPU index
gpu_index_flat = faiss.index_cpu_to_gpu(res, 0, index_flat)

gpu_index_flat.add(xb)         # add vectors to the index
print(gpu_index_flat.ntotal)

k = 4                          # we want to see 4 nearest neighbors
D, I = gpu_index_flat.search(xq, k)  # actual search
print(I[:5])                   # neighbors of the 5 first queries
print(I[-5:])                  # neighbors of the 5 last queries
