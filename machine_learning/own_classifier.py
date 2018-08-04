from scipy.spatial  import distance

def euc(a, b):
    return distance.euclidean(a, b)

class ClassifyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        prediction = []

        for row in X_test:
            lable = self.closest(row)
            prediction.append(lable)
        return prediction

    def closest(self, row):
        best_dist = euc(row, X_train[0])
        best_inx = 0
        for i in range(1, len(X_train)):
            dist = euc(row, X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_inx = i
        return self.y_train[best_inx]


from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

#from sklearn import neighbors
#my_classifier = neighbors.KNeighborsClassifier()

my_classifier = ClassifyKNN()
my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, predictions))

print('HEllo World')
