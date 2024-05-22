# final-project-jhamb_santhosh_finalproject

P1) Design a Web Server running a Web API service that accepts data from distributed sources (e.g.
mobile phones, computers, sensors) into a persistent datastore
Steps involved:
1. Download csv data from kaggle.com (train dataset)
2. Create empty table in sqlite DB browser
3. Import csv dataset to DB browser. Check that str and int variables are differentiated/ make changes. Name file housing.db
4. Set up main.py in VS code using web-api environment. (Check /p1/main.py)
5. Check locally if API is functional using uvicorn main:app
6. ssh into oracle cloud server (already set up)
7. Clone repository containing main.py and housing.db
8. Install necessary packages for web-api environment (uvicorn, fastapi, gunicorn, databases, iosqlite)
9. Restart nginx, run uvicorn and test at https://(domainname)/myapp
10. Test (domainname)/myapp/docs as well as (domainname)/myapp/readings

P2) Use an existing Web API to integrate relevant, publicly accessible, real-time data (e.g. a
Weather API)
Steps involved:
1. Visit Data USA api https://datausa.io/about/api/ and get api call according to variables you want data on. For example for housing property values in various buckets, call https://datausa.io/api/data?measure=Property%20Value%20by%20Bucket,Property%20Value%20by%20Bucket%20Moe&geo=04000US19,01000US&drilldowns=Value%20Bucket
2. Convert format to json and then convert to dataframe
3. Remove irrelevant columns from data and extract latest data from 2019
4. Repeat the process for remaining 4 api calls

P3) Use one or more computational notebooks and/or scripts to prepare data for analysis/sharing, including exploratory visualizations of data.

Steps involved:
1. Using training data from Kaggle.com , we first identify the numerical and categorical variables.
2. Look at the columns with missing data
3. Find the percentage of missing values in each column with data
4. We use 3 strategies to deal with missing values: For categorical variables : we replace the NA values with the imputed mode of the data. For Numerical variables : we replace the NA values with the imputed mean. For variables with too many missing values, we drop them off.
5. To visualize the relationship between the variables and target variable, we use box plots for categorical data and scatter plots for numerical data.

P4)- Use one or more computational notebooks to analyze data to some valuable end, including exploratory and explanatory visualizations, models built from the data through machine learning algorithms, and evaluations of model performance (where applicable). 
objective here, is to predict the Sale price of each house based on the house characteristics. For each Id in the test dataset, we must predict a Sale Price corresponding to it.

Steps involved:
1. We use two datasets called train and test from kaggle.com.
2. Using training data, we check the correlations of each variable with target variable. 
3. Varaibles which have a strong correlation with the target varaible are chosen and defined as main_features.Two datasets X and y are created using data on main_features.
4. X and y dataset are partitioned into training and testing data using test_size = 0.5 and random_state =8000.
5. From the test data, we create x_test dataset, which we use for predictions.
6. We run three regression models- Linear Model, Random Forest and Decision tree regressor and check the accuracy of prediction for each of the models as well as calculate the Mean Absolute Error and Root Mean Squared Error.





