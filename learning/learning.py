from sklearn.naive_bayes import MultinomialNB
import joblib
from export import export_model_to_cpp

X_train = [[1, 0, 0, 1],
           [1, 1, 0, 0],
           [0, 0, 0, 1],
           [1, 1, 0, 1],
           [1, 1, 1, 1]]
y_train = ['a', 'b', 'c', 'd', 'e']  # основные данные (для примера)

multi_model = MultinomialNB()  # создаем модель
multi_model.partial_fit(X_train, y_train, classes=['a', 'b', 'c', 'd', 'e', 'g'])  # обучаем
pred1 = multi_model.predict([[1, 0, 1, 1]])  # прогнозируем
print(pred1)

export_model_to_cpp(multi_model)

joblib_file = "save_model/joblib_model.pkl"
joblib.dump(multi_model, joblib_file) # сохраняем модель в виде файла

new_X_train = [[1, 5, 1, 6],
               [9, 8, 7, 6],
               [7, 6, 5, 4],
               [15, 15, 15, 15]]
new_y_train = ['g', 'g', 'g', 'g']

old_multi_model = joblib.load(joblib_file) # импортируем модель из файла
old_multi_model.partial_fit(new_X_train, new_y_train) # ДОобучаем
pred2 = old_multi_model.predict([[7, 6, 5, 4]])  # прогнозируем
print(pred2)

export_model_to_cpp(old_multi_model)  # экспортируем модель в с++
