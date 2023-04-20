from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import string
import re

class Process:
    """
    Static class to handle preprocessing of data
    """
    def prettyprint(func):
        """"
        function wrapper to print function name before execution
        """
        def wrapper(*args, **kwargs):
            if (func.__name__ == "all"):
                print("Lemmatizing, removing stop words, and cleaning text...")
            print(f"Processing {func.__name__}...")
            return func(*args, **kwargs)
        return wrapper

    # @prettyprint
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
        return ' '.join(filtered_sentence)

    # @prettyprint
    @staticmethod
    def stem_words(text):
        """
        effects: stems words in given string
        text: string
        """
        tokens = word_tokenize(text)
        stemmer = SnowballStemmer('english')
        stemmed_sentence = [stemmer.stem(w) for w in tokens]

        return ' '.join(stemmed_sentence)
    
    # @prettyprint
    @staticmethod
    def lem_words(text):
        """
        effects: lemmatizes words in given string
        text: string
        """
        tokens = word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        lemmatized_sentence = [lemmatizer.lemmatize(w) for w in tokens]

        return ' '.join(lemmatized_sentence)

    @staticmethod
    def clean_punctuation(text):
        """
        effects: removes punctuation from given string
        text: string
        """
        custom_punctuation = string.punctuation.replace("#", "")
        return ''.join([c for c in text if c not in custom_punctuation])
    
    @staticmethod
    def lower_case(text):
        """
        effects: converts text to lowercase
        text: string
        """
        return text.lower()
    

    """
    Regex string manipulation functions
    """

    @staticmethod
    def clean_whitespace(text):
        """"
        effects: substitutes multiple whitespaces with singular space 
        text: string
        """
        return re.sub("\s+", " ", text)

    @staticmethod
    def clean_integers(text):
        """
        effects: substitutes integers with pound sign
        text: string
        """
        return re.sub("\d+", "#", text)
    
    @staticmethod
    def clean_html(text):
        return re.sub("<.*?>", "HTML_TEXT", text)
    
    @staticmethod
    def clean_urls(text):
        return re.sub("http\S+", "URL", text)
    
    @staticmethod
    def clean_emails(text):
        return re.sub("\S+@\S+", "EMAIL", text)
    
    # @prettyprint
    @staticmethod
    def clean_everything(text):
        split = Process.clean_whitespace(Process.clean_urls(Process.clean_emails(text)))
        return Process.clean_punctuation(Process.clean_integers(Process.clean_html(split)))
    
    """
    main function that runs all (default stack) preprocessing functions
    """
    # @prettyprint
    @staticmethod
    def all(text):
        return Process.lower_case(Process.lem_words(Process.stop_word_removal(Process.clean_everything(text))))