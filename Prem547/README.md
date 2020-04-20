### Project Overview

 For this project we will be exploring the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back


### Learnings from the project

 After completing this project, I have a better understanding of how to build a decision tree model,
Train-test split
Correlation between the features
Decision Tree Modeling
Evaluation Metrics
Graphviz plotting


### Approach taken to solve the problem

 Firstly, I've loaded the data and read the columns thoroughly to get a better understanding on data.
I've dropped two columns which are not much useful in our model,
using train_test_split() i've splitted the data into X_train,X_test,y_train,y_test,
To  know the percentage of Borrowers who paid bae the full loan i've plotted a bar plot and got to know that 5639 people have paid back loan while 1065 people not paid back the loan,
along with one step of feature engineering, I had split the features based on the data type for visualization purposes.
I've visualized Numerical Features and Categorical Features Visualisation have successfully plotted (bar plot) against the target variable.known the major reason that stands common for the majority of customers who have applied for a loan is debt_consolidation which means taking one loan to payoff there other loans.
Finally I built the decision tree modeling and have successfully trained data with Decision Tree and found out its accuracy to be 0.73%.
I have successfully pruned the Decision Tree model using Grid Search and found out its accuracy to be 0.837% and
Finally, I've Visualized the pruned tree  using graphviz


### Challenges faced

 NA


### Additional pointers

 NA


