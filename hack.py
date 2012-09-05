import competition_utilities as cu
import features
from sklearn.ensemble import RandomForestClassifier
import numpy as np

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

def words(text):
    return text.split(" ")

def hack():
    print("Reading the data")
    data = cu.get_dataframe(train_file)

    counter = defaultdict(lambda: defaultdict(lambda: 0))
    grouped = data.groupby('OpenStatus')

    for name, group in grouped:
     print name
     for word in group["BodyMarkdown"].apply(words):
        counter[name][word]+=1


if __name__=="__main__":
    hack()