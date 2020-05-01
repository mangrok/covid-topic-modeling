from tweet_lda import TweetLDA
from pprint import pprint


if __name__ == "__main__":
    tlda = TweetLDA()


    tlda.collect_documents()
    tlda.preprocess_documents()

    model, corpus = tlda.generate_model()

    pprint(model.top_topics(corpus))