import bentoml

iris_clf = bentoml.sklearn.get("iris_clf:latest").to_runner()
iris_clf.init_local()
print(iris_clf.predict.run([[5.1, 4.5, 1.4, 0.2]]))