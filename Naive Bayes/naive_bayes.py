#-------------------------------------------------------------------------
# AUTHOR: Tim Hsieh
# FILENAME: naive_bayes.py
# SPECIFICATION: Using Naive Bayes for classification.
# FOR: CS 4210- Assignment #2
# TIME SPENT: 5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here
training_data = []
with open('weather_training.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        training_data.append(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
outlook_mapping = {"Sunny": 1, "Overcast": 2, "Rain": 3}
temperature_mapping = {"Hot": 1, "Mild": 2, "Cool": 3}
humidity_mapping = {"High": 1, "Normal": 2}
wind_mapping = {"Weak": 1, "Strong": 2}
play_tennis_mapping = {"No": 1, "Yes": 2}

# Function to transform categorical data to numerical values
def transform_categorical(data, categories):
    return [categories.index(item) for item in data]

# Function to calculate classification confidence
def calculate_confidence(probabilities):
    return max(probabilities)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
X = []
Y = []
for row in training_data:
    outlook = outlook_mapping[row[1]]
    temperature = temperature_mapping[row[2]]
    humidity = humidity_mapping[row[3]]
    wind = wind_mapping[row[4]]
    play_tennis = play_tennis_mapping[row[5]]
    X.append([outlook, temperature, humidity, wind])
    Y.append(play_tennis)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
test_data = []
with open('weather_test.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        test_data.append(row)

#printing the header os the solution
#--> add your Python code here
print("Day Outlook Temperature Humidity Wind PlayTennis Confidence")

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for row in test_data:
    outlook = outlook_mapping[row[1]]
    temperature = temperature_mapping[row[2]]
    humidity = humidity_mapping[row[3]]
    wind = wind_mapping[row[4]]
    
    # Make probabilistic prediction
    probabilities = clf.predict_proba([[outlook, temperature, humidity, wind]])[0]
    confidence = calculate_confidence(probabilities)
    prediction = "Yes" if clf.predict([[outlook, temperature, humidity, wind]])[0] == 2 else "No"
    
    # Print the result if confidence is >= 0.75
    if confidence >= 0.75:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {prediction} {confidence:.2f}")

