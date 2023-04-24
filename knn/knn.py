
from gensim.models import KeyedVectors

vectors = KeyedVectors.load(
    './word2vec-isl/IGC_2021_lemmatized__350__13__9__5__0_05__1_vectors.kv')


vector = vectors['talva']  # Get numpy vector of a word

query = "pabbi"

data = ['api', 'banani', 'mamma', 'pabbi']

score = []
for i in range(len(data)):
    similarity = vectors.similarity(query, data[i])
    score.append([similarity, i])

score.sort()

for item in score:
    print(item[0], data[item[1]])
