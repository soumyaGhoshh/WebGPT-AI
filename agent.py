import wikipedia
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def search_and_summarize(query):
    try:
        raw_text = wikipedia.summary(query, sentences=5)
        summary = summarizer(raw_text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        return "Sorry, I couldn't find anything useful. Try being more specific."