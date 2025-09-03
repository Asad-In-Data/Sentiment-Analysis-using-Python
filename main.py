from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from newspaper import Article

import nltk
nltk.download('punkt_tab')

url = 'https://en.wikipedia.org/wiki/English_language'
article = Article(url)
article.download()
article.parse()
article.nlp()

text= article.summary
authors=article.authors
print(text)
print(authors)
