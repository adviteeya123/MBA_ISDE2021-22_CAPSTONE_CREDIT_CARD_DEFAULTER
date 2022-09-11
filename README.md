# MBA_ISDE2021-22_CAPTSOTNE_CREDIT_CARD_DEFAULTER
To build a classification methodology to determine whether a person defaults the credit card payment for the next month. 

## Start CAPSTONE - ML - PROJECT 

We will build a machile learning project and deploy to cloud environment. 
We will get an API and we will do the predictions.
Different sections in the project

1. Problem statement
    What is the problem given to us by the client.
2. Description of the data
    What is the data given to us by the client.
    What will be the individual columns and what will be the target columns.
    What is the meaning of the individual columns.
3. Application architechture and module division
    What will be the modules.
    Divide the bigger problems into smaller modules and solve it.
4. Code Explanation
   After having the theoretical background of the prblem we will go with the coding. Various steps involved in the coding are as follows. 
   # a. Data Ingestion
   We will get the data from the client using the mechanism listener to read the data from the topic/database or file poling as suggested by the client or as per the agreement.
   Once we get the data then we check the details of the data or do the validation of the data weather it is as per the agreement by the client. If it is as per the client requirements we will accept the data and put it forward for data preprocessing if not we reject the data and put it in a different folder. 

   # b. Data Preprocessing
   Data cleaning weather the data is 
   i.  normally distributed or not
   ii. how to fill the missing values
   iii.hot to convert the categorical variable to non categorical variable
   iv. if there is any imbalance in the data how to overcome the imbalance in the data over sampling or under sampling
   So whatever techniques is required to clean the data we will use it and perform the same in data preprocessing.

   # c. Model Selection
   Once the data is preprcessed we will diving the data into clusters and apply models on the clusters.
   e.g. one one cluster XG boost , other cluster gradient boost etc.
   After that we go for model tuning.

   # d. Model Tuning
   Out of all these models we will go for hyper parameter tuning and will go for the best model for the particular cluster.
   And we saved the particular model.
   After that we go for the prediction.

   # e. Prediction 
   After we select the model we go for the predictions based on the model we have saved. 
   Again all the data preprocessing steps have to be performed again that we dont during the training.
   Once the data is preprocessed again we will pass it to the clustering algorithm and we will predict the cluster number to which cluster a particular row below after that we will select the ML model for that particular cluster using that model we will do the prediction and then we will combine all the predictions and put it in to a csv file or save it to a file location from where the client can pole or you can post it to a stream we can go as per the client requirements.

   # f. Logging Framework
   Whatever we are doing all the operation should be logged. 
   So that we can keep track of the steps.

   # g. Deployment
   Once all the coding is done we will go for the cloud deployement and shared the API link to the client. 










### Software and Account requirements

Creating conda environment

```
conda create -p venv python==3.7 -y

```
conda activate venv/
```
OR 
```
conda activate venv
```
```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main

and 

git push to update the pending branch
```

'''
about main.py
it consists of 3 routes
# homepage
# training 
# prediction 
'''

LOGGING OF THE FILE
'''
We need to login each and every step. 
So that the support team has better ease of access of our application.
For erroneous situation and exception.
Easy to locate when it was failed and what time it was failed and which file caused the failure.

We have use applicaiton_logging folder to log the file in which logger.py python coding is done

Several ways to perform logging 
1. Logs to a file 
2. Logs to a database
3. Logs to a topic ( listner and consumer will be listening) etc.
4. Custom logging framework

In this project we will be writing our own custom framework.
'''


VALIDATION AND TRANSFORMATION

'''
Validation: Here we have to check weather the data which have been sent to us by the client is valid or not.
We will check our constraints and if the validation rule pass we will put the data into good raw data folder and if the constrains failed we will put it into bad raw data folder (archieved).

From the good raw data folder we will put it into the database and convert it into a form of table.
And then we will export the csv file as an input for the training data

It will be a json file either given by the client or you can create by your own after discussing with the client.
e.g. schema_training.json

Various constraints taken in the project are :
1. Length of the file
2. Check any missing values
3. Length of the column

TRANSFORMATION:

for e.g. sql does not understand the NAN values it understands the NULL values so that type of transformation has been done.
 
'''

DB Operation

'''
GOOD RAW DATA FOLDER AND BAD RAW DATA FOLDER ARE THE temporary FOLDERS JUST FOR INSERTION AND DELETION OF THE FILES

'''

