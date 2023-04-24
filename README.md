# supreme-octo-waffle K-nn and FAISS

Uses word2vec embeddings and faiss to find the kth nearest neighbors of a given word. The embeddings can be found here https://clarin.is/. They were created by Friðriksdóttir, Steinunn Rut ; Daníelsson, Hjalti and Steingrímsson, Steinþór.

dependencies:

```bash
pip install gensim
pip install faiss-cpu
```

download data

```bash
 curl --remote-name-all https://repository.clarin.is/repository/xmlui/bitstream/handle/20.500.12537/209{/word2vec_models.zip}

 unzip /work/word2vec_models.zip
```
