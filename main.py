from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics.cluster import normalized_mutual_info_score, adjusted_rand_score
from sentence_transformers import SentenceTransformer
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

import umap

from sklearn.manifold import TSNE


stop_words = stopwords.words('english') # définir les stop_words
lemmatizer = WordNetLemmatizer()

def dim_red(mat, p, method, labels):
    '''
    Perform dimensionality reduction

    Input:
    -----
        mat : NxM list
        p : number of dimensions to keep
    Output:
    ------
        red_mat : NxP list such that p<<m
    '''
    if method=='ACP':
          # Initialize PCA object
        pca = PCA(n_components=20)

        # Fit PCA on embeddings
        pca.fit(mat)

        # Apply dimensionality reduction
        df_pca = pd.DataFrame(pca.transform(mat))

        # Add label column to the new dataframe
        df_pca['label'] = labels

        # Rename columns
        df_pca.columns = ['PCA'+str(i+1) for i in range(p)] + ['label']

        red_mat = df_pca

    elif method=='UMAP':
            # Initialize UMAP object
            umap_obj = umap.UMAP(n_components=p)

            # Fit PCA on embeddings
            umap_obj.fit(mat)

            # Apply dimensionality reduction
            df_umap = pd.DataFrame(umap_obj.transform(mat))

            # Add label column to the new dataframe
            df_umap['label'] = labels

            # Rename columns
            df_umap.columns = ['UMAP'+str(i+1) for i in range(p)] + ['label']

            red_mat = df_umap

    elif method=='t-SNE':
      # Initialize  object
        tsne = TSNE(n_components=3)
        df_tsne = pd.DataFrame(tsne.fit_transform(mat))
        df_tsne['label'] = df_labels['label']
        df_tsne.columns = ['x', 'y','z', 'label']
        red_mat = df_tsne

    else:
        raise Exception("Please select one of the three methods : APC, AFC, UMAP")

    return red_mat


def kmeans_method(data, labels,  num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    kmeans.fit(data)
    kmeans_labels = kmeans.labels_

    return kmeans_labels

def load_data():
    ng20 = fetch_20newsgroups(subset='test')
    corpus = ng20.data[:2000]
    labels = ng20.target[:2000]
    df_labels = pd.DataFrame(labels)
    df_labels.rename(columns = {0:'label'}, inplace = True)
    df_corpus = pd.DataFrame(corpus)
    df_corpus.rename(columns = {0:'text'}, inplace = True)
    return df_corpus, df_labels

def data_preprocessing(review):

  # nettoyage des données
  article = re.sub(re.compile('<.*?>'), '', review) #removing html tags
  article =  re.sub('[^A-Za-z0-9]+', ' ', review) #taking only words

  # miniscule
  article = article.lower()

  # tokenization
  tokens = nltk.word_tokenize(article) # converts articles to tokens

  # stop_words removal
  article = [word for word in tokens if word not in stop_words] #removing stop words

  # lemmatization
  article = [lemmatizer.lemmatize(word) for word in article]

  # join words in preprocessed review
  article = ' '.join(article)

  return article





df_corpus, df_labels = load_data()
df_corpus['preprocessed_text'] = df_corpus['text'].apply(lambda article: data_preprocessing(article))





# embedding
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

embeddings = model.encode(df_corpus['preprocessed_text'])


# Perform dimensionality reduction and clustering for each method
methods = ['UMAP', 't-SNE','ACP']
for method in methods:
    # Perform dimensionality reduction
    red_emb = dim_red(embeddings, 20, method, df_labels)
    
    # Perform clustering
    pred = kmeans_method(red_emb, df_labels,  3)

    # Evaluate clustering results
    nmi_score = normalized_mutual_info_score(pred, df_labels['label'])
    ari_score = adjusted_rand_score(pred, df_labels['label'])


    # Print results
    print(f'Method: {method}\nNMI: {nmi_score:.2f} \nARI: {ari_score:.2f}\n')
