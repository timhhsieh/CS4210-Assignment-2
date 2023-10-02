#-------------------------------------------------------------------------
# AUTHOR: Tim Hsieh
# FILENAME: decision_tree_2.py
# SPECIFICATION: decision tree classifiers on three datasets, tests them, and calculates their average accuracy over 10 iterations for each.
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    for instance in dbTraining:
        x_instance = []
        for i in range(4):
            if instance[i] == 'Young':
                x_instance.append(1)
            elif instance[i] == 'Prepresbyopic':
                x_instance.append(2)
            elif instance[i] == 'Presbyopic':
                x_instance.append(3)
            else:
                x_instance.append(0)  # Handle unknown values as 0
        X.append(x_instance)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    for instance in dbTraining:
        if instance[4] == 'Yes':
            Y.append(1)
        elif instance[4] == 'No':
            Y.append(2)

    accuracy_sum = 0

    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       dbTest = []
       with open('contact_lens_test.csv', 'r') as testfile:
            testreader = csv.reader(testfile)
            for j, test_row in enumerate(testreader):
                if j > 0:  # skipping the header
                    dbTest.append(test_row)

       correct_predictions = 0
       
       for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
            x_test_instance = []
            for i in range(4):
                if data[i] == 'Young':
                    x_test_instance.append(1)
                elif data[i] == 'Prepresbyopic':
                    x_test_instance.append(2)
                elif data[i] == 'Presbyopic':
                    x_test_instance.append(3)
                else:
                    x_test_instance.append(0)  # Handle unknown values as 0

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
            class_predicted = clf.predict([x_test_instance])[0]
            if class_predicted == 1 and data[4] == 'Yes':
                correct_predictions += 1
            elif class_predicted == 2 and data[4] == 'No':
                correct_predictions += 1
        # Calculate accuracy for this run
       accuracy = correct_predictions / len(dbTest)
       accuracy_sum += accuracy

    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    average_accuracy = accuracy_sum / 10


    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print(f'Final accuracy when training on {ds}: {average_accuracy:.2f}')

# Final accuracy when training on contact_lens_training_1.csv: 0.38
# Final accuracy when training on contact_lens_training_2.csv: 0.75
# Final accuracy when training on contact_lens_training_3.csv: 0.75
