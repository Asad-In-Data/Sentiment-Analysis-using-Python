from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from newspaper import Article

# this is for article summarization
# import nltk
# nltk.download('punkt')

# url = 'https://en.wikipedia.org/wiki/English_language'
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()

# text= article.summary
# authors=article.authors
# print(text)
# print(authors)

# now we do it for our text

with open('my_text.txt', 'r') as f:
    text = f.read()



blob=TextBlob(text) # analyzer=NaiveBayesAnalyzer()) # this line of code initializes the TextBlob and NaiveBayesAnalyzer is used for sentiment analysis
sentiment=blob.sentiment.polarity # this line of code calculates the sentiment polarity of the text
print(sentiment)