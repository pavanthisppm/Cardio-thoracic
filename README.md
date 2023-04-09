# Cardio-thoracic

#### Python, HTML, CSS , JavaScript , Flask

This study was conducted to predict survival status of cancer patients who faced to the Cardio thoracic surgery using the machine learning. According to the initial descriptive analysis our target variable ‘survive’ was highly unbalanced. Therefore, we used SMOTE in order to balance the dataset. Then the Logistic Regression, Decision Tree, K Nearest Neighbors, Support Vector Machine were fitted to the dataset, and further to increase F1 score random forest and Voting Classifier models were fitted with hyperparameter tunning techniques. By comparison of F1 scores of all the models, we could notice that applying SMOTE methodology results in poor predictability of data. So, we made the decision to go along with models fitted to original data. Looking at those models, we realized that Logistic Regression, KNN, SVM and Voting Classifier performs exceptionally well. Out of them, considering interpretability and computational cost, we decided to go with the Logistic Regression model, which had an 85.4% F1 score. So, the final model that we used for our data product was the Logistic Regression model without SMOTE. In addition to a web application, a mobile application was created using MIT App Inventor for the prediction part.



https://user-images.githubusercontent.com/96905837/230759786-ac7fb995-0d1f-4ee9-b5da-72754d95d6ac.mp4

