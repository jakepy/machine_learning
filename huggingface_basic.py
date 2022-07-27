## Use the amazing hugging face library to perform basic sentiment analysis.
from transformers import pipeline

classifier = pipeline('sentiment-analysis')

text = input('Text: ')
result = classifier(text)
for k in result:
    label = k['label'].capitalize()
    score = round(k['score'], 2) * 100
    print(f"Sentiment: {label}")
    print(f'Confidence: {score}%')
