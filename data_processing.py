import re
import numpy as np
from gensim.models import KeyedVectors

# load pre-trained word2vec embeddings
vectors = KeyedVectors.load(
    './word2vec-isl/IGC_2021_lemmatized__350__13__9__5__0_05__1_vectors.kv')

def load_stop_words(stop_words_path):
    if stop_words_path == '':
        raise ValueError("Stop words path is empty, nothing to load.")
    
    stop_words = set()
    try:
        with open(stop_words_path, "r") as f:
            for line in f:
                stop_words.add(line.strip())
    except:
        raise ValueError("Stop words file not found.")

    return stop_words


def calculate_mean_vector(embeddings):
    """
    calculates mean vectors of data. for similarity search.

    input: np.array data
    output: mean vector
    """
    if embeddings.size < 0:
        raise ValueError("Embeddings are empty, nothing to calculate mean vector of.")
    
    # average of the sum of all the word embeddings
    sum_vec = np.sum(embeddings, axis=0)
    return np.mean(sum_vec)

def convert_to_word_embeddings(data):
    """
    converts to the word embeddings

    input: list of preprocessed data
    output: list of word vectors
    """
    if not data:
        raise ValueError("Data is empty, nothing to tokenize.")

    word_embeddings = []
    for word in data:
        try:
            word_embeddings.append(vectors.get_vector(word, norm=True))
        except KeyError:
            pass

    return word_embeddings

def preprocess(data='', stop_words=None):
    """
    Preprocess data. Removes stop words and punctuation. And returns word embeddings.

    input: str data
    output: word embeddings of the data (stripped of stop words and punctuation)

    time complexity: O(n)
    """
    if data == '':
        raise ValueError("Data is empty, nothing to preprocess.")

    if not stop_words:
        raise ValueError("Stop words not loaded.")
    
    data = data.lower().split(" ")
    data = [re.sub(r'[^\w\s\t\n]','',word) for word in data if word not in stop_words]
    

    # np array for faster processing
    data = np.array(data)

    return data


def save_to_db(mean_vector, text):
    """
    Saves the mean vector and the text to the database.
    """
    if mean_vector.size < 0:
        raise ValueError("Mean vector is empty, nothing to save to the database.")
    
    if text == '':
        raise ValueError("Text is empty, nothing to save to the database.")
    
    with open("./db.txt", "a") as f:
        f.write(f"{mean_vector}\n{text}")

# Load the stop words from file
stop_words = load_stop_words("./stop-words/function-words.txt")

# Preprocess the input text
to_process = "Sigurður segir að í fyrstu hafi aðeins verið talið að einn einstaklingur væri um borð, en síðan kom á daginn að þeir hafi verið fleiri."
tokens = preprocess(to_process, stop_words)

# Convert the preprocessed text into word embeddings
embeddings = convert_to_word_embeddings(tokens)

# Calculate the mean vector of the word embeddings
mean_vector = calculate_mean_vector(embeddings)

# save to `db.txt`
save_to_db(mean_vector, to_process)
