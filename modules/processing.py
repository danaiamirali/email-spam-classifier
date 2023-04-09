from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

class Process:
    """
    Static class to handle preprocessing of data
    """
    def prettyprint(func):
        def wrapper(*args, **kwargs):
            print(f"Processing {func.__name__}...")
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def stop_word_removal(text):
        """
        effects: removes stop words from given string
        text: string
        """
        # Tokenize text and fetch stop words from NLTK
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        # Remove stop words
        filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
        print(filtered_sentence)
        return ''.join(filtered_sentence)

    @staticmethod
    def stem_words(text):
        """
        effects: stems words in given string
        text: string
        """
        tokens = word_tokenize(text)
        stemmer = SnowballStemmer()
        stemmed_sentence = [stemmer.stem(w) for w in tokens]

        return ''.join(stemmed_sentence)
    
    @staticmethod
    def lem_words(text):
        """
        effects: lemmatizes words in given string
        text: string
        """
        tokens = word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        lemmatized_sentence = [lemmatizer.lemmatize(w) for w in tokens]

        return ''.join(lemmatized_sentence)

    @staticmethod
    def remove_punctuation(text):
        """
        effects: removes punctuation from given string
        text: string
        """
        # return ''.join([c for c in text if c not in string.punctuation])