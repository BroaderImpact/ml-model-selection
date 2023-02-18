from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def select_model():
    """
    Takes input and returns best machine learning model.
    """
    print("Answer the following questions to select a machine learning model:")

    linear = input("Is the target variable continuous? (yes or no) ")
    if linear.lower() == "yes":
        print("Linear Regression is recommended.")
        return LinearRegression()

    classification = input("Are you trying to predict a categorical outcome? (yes or no) ")
    if classification.lower() == "yes":
        random_forest = input("Do you have a large number of features? (yes or no) ")
        if random_forest.lower() == "yes":
            print("Random Forest Classifier is recommended.")
            return RandomForestClassifier()
        else:
            logistic = input("Is the outcome binary? (yes or no) ")
            if logistic.lower() == "yes":
                print("Logistic Regression is recommended.")
                return LogisticRegression()
            else:
                svm = input("Do you have a small or medium-sized dataset? (yes or no) ")
                if svm.lower() == "yes":
                    print("Support Vector Machines is recommended.")
                    return SVC()
                else:
                    print("K-Nearest Neighbors is recommended.")
                    return KNeighborsClassifier()
    else:
        clustering = input("Are you trying to group similar data points? (yes or no) ")
        if clustering.lower() == "yes":
            print("K-Means Clustering is recommended.")
            return KMeans()
        else:
            print("Principal Component Analysis is recommended.")
            return PCA()
