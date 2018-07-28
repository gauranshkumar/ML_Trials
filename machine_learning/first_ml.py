from sklearn import tree

feature = [[150,0],[170,0],[140,1],[130,1]]

lable = ['Orange','Orange','Apple','Apple']

clasifier = tree.DecisionTreeClassifier() #classifier created

clasifier = clasifier.fit(feature, lable)       #Learning Algorithm

print(clasifier.predict([[200,0]]))        #predicting and printing the output
