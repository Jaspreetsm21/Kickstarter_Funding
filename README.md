# Data Science Kickstarter Sucess Rate: Project Overview

* Created a tool that esitmates the success rate of Kickstarter funding project to help entrepreneur understand what feature/element has to achieve a successful campagin.
* Optimised Linear,DecisionTree and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask and Heroku to view that on the web.

# Code and Resources Used

**Python Version**: 3.7

**Packages**: pandas, numpy, sklearn, matplotlib, seaborn, flask, json, pickle

**For Web Framework Requirements**: pip install -r requirements.txt

**Flask and Heroku Production**: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2


# Model Building 
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried four different models and evaluated them using Precision, Recall and confusion matrix. I chose confusion matrix because it is relatively easy to interpret.

I tried four different models:

Linear Logistic – Baseline for the model
Decision Tree and kneighborsclassifier 
Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.


# Model Performance

# Production 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a Kickstarter listing and returns an success rate.
