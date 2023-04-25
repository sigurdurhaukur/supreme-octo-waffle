import re
import numpy as np

STOP_WORDS_PATH = "./stop-words/function-words.txt"
STOP_WORDS = set()

def get_stop_words():
    with open(STOP_WORDS_PATH, "r") as f:
        for line in f:
            STOP_WORDS.add(line.strip())

def preprocess(data='', cache=None):
    """
    Preprocess data.

    input: str data
    output: data stripped of stop words and punctuation

    time complexity: O(n)
    """
    if data == '':
        raise ValueError("Data is empty, nothing to preprocess.")

    if cache is not None and data in cache:
        return cache[data]

    if not STOP_WORDS:
        get_stop_words()

    data = data.lower().split(" ")
    data = [re.sub(r'[^\w\s\t\n]','',word) for word in data if word not in STOP_WORDS]
    
    if cache is not None:
        cache[data] = data

    return data


def get_mean_vector(data):
    """
    Get mean vector of data. for similarity search.

    input: np.array data
    output: mean vector
    """
    # if not data:
    #     raise ValueError("Data is empty, nothing to get mean of.")
    
    # average of the sum of all the word embeddings
    sum_vec = np.sum(data, axis=0)
    return np.mean(sum_vec)

to_process = "Sigurður segir að í fyrstu hafi aðeins verið talið að einn einstaklingur væri um borð, en síðan kom á daginn að þeir hafi verið fleiri."

processed = preprocess(to_process)
processed = np.array(processed)


# pseudo-tokenizer
d = 350
n = len(processed)
processed1 = np.random.rand(n, d).astype('float32')
processed2 = np.random.rand(n, d).astype('float32')
processed3 = np.random.rand(n, d).astype('float32')

print(get_mean_vector(processed1))
print(get_mean_vector(processed2))
print(get_mean_vector(processed3))

