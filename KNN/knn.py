#-------------------------------------------------------------------------
# AUTHOR: Tim Hsieh
# FILENAME: knn.py
# SPECIFICATION: Finds the LOO-CV Error Rate for 1NN in binary_points.csv
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

# Initialize variables to keep track of correct predictions and total predictions
correct_predictions = 0
total_predictions = 0

#loop your data to allow each instance to be your test set
for i, test_instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X = []
    Y = []

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    for j, row in enumerate(db):
        if i != j:
            X.append([float(row[0]), float(row[1])])
            Y.append(1 if row[2] == '+' else 0)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = [float(test_instance[0]), float(test_instance[1])]


    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if (class_predicted == 1 and test_instance[2] == '+') or (class_predicted == 0 and test_instance[2] == '-'):
        correct_predictions += 1
    total_predictions += 1

#print the error rate
#--> add your Python code here
error_rate = (total_predictions - correct_predictions) / total_predictions
print(f"LOO-CV Error Rate for 1NN: {error_rate}")
