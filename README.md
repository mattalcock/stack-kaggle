Benchmarks for Kaggle's [Predict Closed Questions on Stack Overflow](https://www.kaggle.com/c/predict-closed-questions-on-stack-overflow) competition

The benchmarks require several Python packages:

 - numpy
 - pandas
 - sklearn

These packages can be installed with easy_install or pip, or Windows users can [download compiled versions of these packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

To run the benchmarks, you also need to [download the data](https://www.kaggle.com/c/predict-closed-questions-on-stack-overflow/data). The only files necessary for the benchmarks are train-sample.csv and public_leaderboard.csv. Two variables need to be updated in competition_utilities.py as well: data_path should be set to the path to the data, and submissions_path should be set to the location for writing the submission files.


Basic Benchmark
Prior Benchmark
Uniform Benchmark


Basic_Classify = 0.21689
==================================
train_file = "train-sample.csv"
full_train_file = "train.csv"
test_file = "public_leaderboard.csv"
submission_file = "basic_classify.csv"

feature_names = [ "BodyLength"
                , "NumTags"
                , "OwnerUndeletedAnswerCountAtPostTime"
                , "ReputationAtPostCreation"
                , "TitleLength"
                , "TitleWordCount"
                , "UserAge"
                ]
n_estimators=60

Basic_Classify = 
==================================
train_file = "train-A.csv"
full_train_file = "train.csv"
test_file = "public_leaderboard.csv"
submission_file = "basic_classify_v2.csv"

feature_names = [ "BodyLength"
                , "NumTags"
                , "OwnerUndeletedAnswerCountAtPostTime"
                , "ReputationAtPostCreation"
                , "TitleLength"
                , "TitleWordCount"
                , "UserAge"
                ]
n_estimators=60


ssh -i ~/.ec2/ec2.pem ubuntu@ec2-23-23-24-119.compute-1.amazonaws.com
scp test/winning.txt root@my-ec2-public-ip.amazonaws.com:temp-files/