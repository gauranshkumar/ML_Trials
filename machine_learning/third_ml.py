from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import graphviz
iris = load_iris()

test_id = [2,52,102]

#training data separation

train_target = np.delete(iris.target, test_id)
train_data = np.delete(iris.data, test_id, axis=0)

#testing data

test_target = iris.target[test_id]
test_data = iris.data[test_id]

#creating Classifier

cls = tree.DecisionTreeClassifier()

cls = cls.fit(train_data, train_target)

#print(test_target)

#print(cls.predict(test_data))


#gapical vizualization of tree

##dot_data = tree.export_graphviz(cls, out_file=None,
##                         feature_names=iris.feature_names,
##                         class_names=iris.target_names,
##                         filled=True, rounded=True,
##                         special_characters=True,
##                         impurity=False)
##graph = graphviz.Source(dot_data)
##graph.render('iris_color')

print(test_data[1],test_target[1])
print(iris.target_names)
print(iris.feature_names)






