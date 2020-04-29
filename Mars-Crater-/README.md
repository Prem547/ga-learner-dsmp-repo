### Project Overview

 This dataset was generated using HRSC nadir panchromatic image h0905_0000 taken by the Mars Express spacecraft. The images is located in the Xanthe Terra, centered on Nanedi Vallis and covers mostly Noachian terrain on Mars. The image had a resolution of 12.5 meters/pixel.

Determine if the instance is a crater or not a crater. 1=Crater, 0=Not Crater


### Learnings from the project

 I've applied Decision tree, boot strapping method, voting classifier and random forest algorithm and learned how they exactly work.


### Approach taken to solve the problem

 firstly,  i've Loaded the dataset using pandas read_csv api in variable df using file path as path.
Displayed the first 5 columns of dataframe df to know how the data exactly is
Stored all the features(independent values) in a variable called X
Stored the target variable (dependent value) in a variable called y
i had Split the dataframe into X_train,X_test,y_train,y_test using train_test_split() function using parameters as test_size = 0.3 and random_state =4
Initailaized a  MinMaxScaler and stored it in a variable scaler
i had Fit this scaler on the train data using .fit(X_train) and then transformed both the train and test features with .transform() method. Assigned them back to X_train and X_test
I've applied all algorithms like .,
Decision Tree,
Random forrest algorithm,
Bagginng or Bootstrap aggregation and 
finally, Voting Classifier.
I've compared all the scores for the best model



### Challenges faced

 NA


### Additional pointers

 NA


