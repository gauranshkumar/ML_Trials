from sklearn import tree

feature = [[300,2],[450,2],[200,8],[150,9]]
lable = ['Sports Car','Sports Car','Mini Van','Mini Van']

cls = tree.DecisionTreeClassifier()
cls = cls.fit(feature,lable)

print(cls.predict([[800,11]]))
