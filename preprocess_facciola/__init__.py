from preprocess_facciola import utils

__version__ = '0.0.1'

def get_wordcounts(x):
   '''
   get the number of words in the text
   '''
   return utils._get_wordcounts(x)

def get_charcounts(x):
   '''
   get the number of characters in the text
   '''
   return utils._get_charcounts(x)

def get_avg_wordlength(x):
   '''
   get avergae word length in blob of text
   '''
   return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):
   '''
   get count of stop words in text
   '''
   return utils._get_stopwords_counts(x)

def get_hashtag_counts(x):
   '''
   get number of hashtags in text
   '''
   return utils._get_hashtag_counts(x)

def get_mentions_counts(x):
   '''
   return number of mentions in text
   '''
   return utils._get_mentions_counts(x)

def get_digit_counts(x):
   '''
   get number of digits in text
   '''
   return utils._get_digit_counts(x)

def get_uppercase_counts(x):
   '''
   get number of uppercase words in text
   '''
   return utils._get_uppercase_counts(x)

def get_cont_to_exp(x):
   '''
   replace contractions with their expanded form
   '''
   return utils._get_cont_to_exp(x)

def get_emails(x):
   '''
   get emails and number of emails in text
   '''
   return utils._get_emails(x)

def remove_emails(x):
   '''
   remove emails from a blob of text
   '''
   return utils._remove_emails(x)

def get_urls(x):
   '''
   get urls and their counts
   '''
   return utils._get_urls(x)

def remove_urls(x):
   '''
   remove urls from a blob of text
   '''
   return utils._remove_urls(x)

def remove_rt(x):
   '''
   remove retweets from blob of data
   '''
   return utils._remove_rt(x)

def remove_special_chars(x):
   '''
   remove special characters from text
   '''
   return utils._remove_special_chars(x)

def remove_html_tags(x):
   '''
   remove html tags from a blob of text
   '''
   return utils._remove_html_tags(x)

def remove_accented_chars(x):
   '''
   remove accented chars from a blob of těxt
   '''
   return utils._remove_accented_chars(x)

def remove_stopwords(x):
   '''
   remove stop words from a blob of text
   '''
   return utils._remove_stopwords(x)

def lemmatize(x):
   '''
   convert all words in blob of text to their lemma
   '''
   return utils._lemmatize(x)

def remove_commonwords(x, n=20):
   '''
   remove the most frequently occuring words in a blob of text specified by n
   [default is 20]
   '''
   return utils._remove_commonwords(x,n)

def remove_rarewords(x, n=20):
   '''
   remove the least frequently occuring words in a blob of text specified by n
   [default is 20]
   '''
   return utils._remove_rarewords(x, n)

def visualize_words(text, **kwargs):
   '''
   generates a visualization of word count in text
   '''
   return utils._visualize_words(text, kwargs)

def spelling_correction(x):
   '''
   replaces mispelled words with correctly spelled words
   '''
   return utils._spelling_correction(x)

def get_nouns(x):
   '''
   gets nouns in text and their counts
   '''
   return utils._get_nouns(x)

def detect_lang(x):
   '''
   attempts to detect the language of x
   '''
   return utils._detect_lang(x)

def translate_to(x, to = 'es'):
   '''
   return translated text based on iso 639 code [default is spanish]
   '''
   return utils._translate_to(x, to)