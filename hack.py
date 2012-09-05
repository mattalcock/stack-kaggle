import competition_utilities as cu
import features
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from collections import defaultdict
import operator
from stop import STOP_WORDS

train_file = "train-sample.csv"
full_train_file = "train.csv"
test_file = "public_leaderboard.csv"
submission_file = "basic_benchmark.csv"

feature_names = [ "BodyLength"
                , "NumTags"
                , "OwnerUndeletedAnswerCountAtPostTime"
                , "ReputationAtPostCreation"
                , "TitleLength"
                , "UserAge"
                ]

STOP_WORD_SET = set(STOP_WORDS)

def words(text, limit=3):
    word_list = []
    for w in text.split(" ")
        if len(w) > limit and w not in STOP_WORD_SET:
            word_list.append(w)
    return word_list

def hack():
    print("Reading the data")
    data = cu.get_dataframe(train_file)

    counter = defaultdict(lambda: defaultdict(lambda: 0))
    grouped = data.groupby('OpenStatus')

    for name, group in grouped:
     print name
     for wrds in group["BodyMarkdown"].apply(words):
        for word in wrds:
            counter[name][word]+=1

    limit = 20
    for name, word_dict in counter.items():
        for word, count in sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)[:limit]
            print name, word, count

if __name__=="__main__":
    hack()