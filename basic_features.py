import competition_utilities as cu
import csv
import datetime
import basic_features as features 
import numpy as np
import pandas as pd
import re

def camel_to_underscores(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def words(text):
    return text.split(" ")
    
def nouns():
    pass

def word_count(text):
    return len(words(text))



##############################################################
###### FEATURE FUNCTIONS
##############################################################

def body_length(data):
    return pd.DataFrame.from_dict({"BodyLength": data["BodyMarkdown"].apply(len)})

def num_tags(data):
    return pd.DataFrame.from_dict({"NumTags": [sum(map(lambda x:
                    pd.isnull(x), row)) for row in (data[["Tag%d" % d
                    for d in range(1,6)]].values)] } ) ["NumTags"]

def title_length(data):
    return pd.DataFrame.from_dict({"TitleLength": data["Title"].apply(len)})

def title_word_count(data):
    return pd.DataFrame.from_dict({"TitleWordCount": data["Title"].apply(word_count)})

def user_age(data):
    return pd.DataFrame.from_dict({"UserAge": (data["PostCreationDate"]
            - data["OwnerCreationDate"]).apply(lambda x: x.total_seconds())})

###########################################################

def extract_features(feature_names, data):
    fea = pd.DataFrame(index=data.index)
    for name in feature_names:
        if name in data:
            fea = fea.join(data[name])
        else:
            fea = fea.join(getattr(features, 
                camel_to_underscores(name))(data))
    return fea

if __name__=="__main__":
    feature_names = [ "BodyLength"
                    , "NumTags"
                    , "OwnerUndeletedAnswerCountAtPostTime"
                    , "ReputationAtPostCreation"
                    , "TitleLength"
                    , "TitleWordCount"
                    , "UserAge"
                    ]
              
    data = cu.get_dataframe("train-sample.csv")
    features = extract_features(feature_names, data)
    print(features)