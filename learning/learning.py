import sklearn_json as skljson
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

X_train, y_train = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 2, 3, 4], [4, 3, 2, 1]], [1, 2, 3, 4]  # for example

multi_model = MultinomialNB()

multi_model.fit(X_train, y_train)  # training

skljson.to_json(multi_model, 'model.json')  # export to json

multi_model = skljson.from_json('model.json')  # import from json
