

########################################################################################################
#
#   Sklearn Modeling
#
########################################################################################################

import os,sys,csv,re
import time,datetime

import pandas as pd
import numpy as np
import scipy as sp

from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import explained_variance_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeClassifier

########################################################################################################
#
#   Global Functions - Used for both Model Building and Model Scoring
#
########################################################################################################




########################################################################################################
#
#   Input Data
#
########################################################################################################

col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
data = pd.read_csv('/tmp/adult.data.txt', header=None, names=col_names)

########################################################################################################
#
#   Descriptive Stats
#
########################################################################################################

data.head()
data.iloc[0]
data.columns
data.dtypes
data.shape

transformed_df['education'].value_counts()
transformed_df['marital_status'].value_counts()
data.describe()

########################################################################################################
#
#   Model Variables (Specify id, target, numeric variables, and categorical variables)
#
########################################################################################################

data['target'] = data['income'].apply(lambda x: 1 if x.strip() == '>50K' else 0)

var_id              = None
var_target          = 'target'
var_date            = None
list_unused         = ['income']
list_numeric        = [col[0] for col in data.dtypes.iteritems() if (col[1].name in ['int64','uint64','float64']) and (col[0] not in ([var_id, var_target, var_date]+list_unused))]
list_category       = [col[0] for col in data.dtypes.iteritems() if (col[1].name in ['object']) and (col[0] not in ([var_id, var_target, var_date]+list_unused)) ]

########################################################################################################
#
#   Transformations
#
########################################################################################################

# Strip Whitespace
data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Derive Data vars, if date exists
if var_date != None:
    data['year']    = pd.to_datetime(data[var_date]).dt.year
    data['month']   = pd.to_datetime(data[var_date]).dt.month
    data['day']     = pd.to_datetime(data[var_date]).dt.day

def education_groupings(df):
    if df['education'] == '12th' or df['education'] == '11th' or df['education'] == '10th' or df['education'] == '9th':
        group = 'some-HS'
    elif df['education'] == 'Preschool' or df['education'] == '1st-4th' or df['education'] == '5th-6th' or df['education'] == '7th-8th':
        group = 'dropout-before-HS'
    elif df['education'] == 'Assoc-voc' or df['education'] == 'Assoc-acdm':
        group = 'associates'
    else:
        group = df['education']
    return group 

transformed_df = data
transformed_df['education'] = transformed_df.apply(education_groupings, axis=1)
transformed_df['education'].value_counts()

def marital_groupings(df):
    if df['marital_status'] == 'Married-civ-spouse' or df['marital_status'] == 'Married-AF-spouse' or df['marital_status'] == 'Married-spouse-absent':
        group = ' Married'
    elif df['marital_status'] == 'Divorced' or df['marital_status'] == 'Separated' or df['marital_status'] == 'Widowed':
        group = ' Not-married'
    else:
        group = df['marital_status']
    return group

transformed_df['marital_status'] = transformed_df.apply(marital_groupings, axis=1)
transformed_df['marital_status'].value_counts()

# Get Dummies
transformed_df = pd.get_dummies(data, columns=list_category)
transformed_df.shape
transformed_df.drop( (list_unused), axis=1, inplace=True)
transformed_df.shape

# Fill na
transformed_df = transformed_df.fillna(-1)

########################################################################################################
#
#   Train and Test DFs
#
########################################################################################################

random_number  = pd.DataFrame(np.random.randn(len(transformed_df), 1))
partition_mask = np.random.rand(len(random_number)) <= 0.75

train_data     = transformed_df[partition_mask]
test_data      = transformed_df[~partition_mask]

train_data.shape
test_data.shape

train_target   = train_data[var_target]
train_inputs   = train_data.drop([var_target], axis=1)

test_target    = test_data[var_target]
test_inputs    = test_data.drop([var_target], axis=1)


########################################################################################################
#
#   Decision Tree (Classifier)
#
########################################################################################################

dt = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=99)
dt.fit(train_inputs, train_target)

test_predicted = dt.predict(test_inputs)

from sklearn.metrics import accuracy_score
accuracy_score(test_target, test_predicted)

from sklearn.metrics import confusion_matrix
confusion_matrix(test_target, test_predicted)

import pickle
pickle.dump(dt, open('/tmp/dt.sav', 'wb'))
#dt_saved = pickle.load(open('/tmp/dt.sav', 'rb'))
#predicted = dt_saved.predict(df)

#from sklearn.externals import joblib
#joblib.dump(df, '/tmp/dt.sav')
#dt_saved = joblib.load('/tmp/dt.sav')
#predicted = dt_saved.predict(df)


#ZEND
