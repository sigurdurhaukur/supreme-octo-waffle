from isl_wiki import get_wikipedia_articles
from api.data_processing import vectorize_sync as vectorize
from sentence_transformers import SentenceTransformer
import numpy as np

# Retrieve Wikipedia articles
data = get_wikipedia_articles(max_articles=None)

# Load Sentence Transformer model
medium_model = SentenceTransformer("./api/isl-tsdae-m/tsdae-bert-base-uncased")

# Embed each article's summary
embeddings_array = []
articles_array = []


def embedd(article, model):
    text = article.summary
    if model == "TSDAE":
        return medium_model.encode([text])[0]
    elif model == "word2vec":
        vectors = vectorize(text)
        return vectors[0]


for article in data:
    try:
        # Embed the summary and save the article title
        embedding = embedd(article, model="word2vec")
        embeddings_array.append(embedding)
        articles_array.append(article.title)
    except:
        pass

# Convert to numpy arrays
embeddings_array = np.array(embeddings_array)
articles_array = np.array(articles_array)

# Save embeddings and metadata
np.savetxt(
    "./visualizing-embeddings/word2vec-embeddings.tsv",
    embeddings_array,
    delimiter="\t",
    fmt="%f",
)
np.savetxt(
    "./visualizing-embeddings/word2vec-metadata.tsv",
    articles_array,
    delimiter="\n",
    fmt="%s",
)
