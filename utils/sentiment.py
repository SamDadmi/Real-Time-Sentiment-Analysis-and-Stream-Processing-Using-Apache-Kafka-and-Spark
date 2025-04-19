def map_label_to_sentiment(label):
    if label == 1:
        return "positive"
    elif label == -1:
        return "negative"
    else:
        return "neutral"

