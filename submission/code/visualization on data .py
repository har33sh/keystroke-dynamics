
# coding: utf-8

# # Analysis on the keystroke-timing dataset
# 
#  ### Click here for [Dataset](http://www.cs.cmu.edu/~keystroke/)
# 
# 
# ## Information about the data
# The data are arranged as a table with 34 columns. Each row of data corresponds to the timing information for a single repetition of the password by a single subject. The first column, subject, is a unique identifier for each subject (e.g., s002 or s057). Even though the data set contains 51 subjects, the identifiers do not range from s001 to s051; subjects have been assigned unique IDs across a range of keystroke experiments, and not every subject participated in every experiment. For instance, Subject 1 did not perform the password typing task and so s001 does not appear in the data set. The second column, sessionIndex, is the session in which the password was typed (ranging from 1 to 8). The third column, rep, is the repetition of the password within the session (ranging from 1 to 50).
# 
# The remaining 31 columns present the timing information for the password. The name of the column encodes the type of timing information. Column names of the form H.key designate a hold time for the named key (i.e., the time from when key was pressed to when it was released). Column names of the form DD.key1.key2 designate a keydown-keydown time for the named digraph (i.e., the time from when key1 was pressed to when key2 was pressed). Column names of the form UD.key1.key2 designate a keyup-keydown time for the named digraph (i.e., the time from when key1 was released to when key2 was pressed). Note that UD times can be negative, and that H times and UD times add up to DD times.
# 

# In[1]:

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')
# Reading the Password data into dataframes
df = pd.read_csv("../data/PasswordData.csv")
#getting to know about the data
# df.info()  


# ## Gaussian Model for first 3 users

# In[11]:

from scipy.stats import norm
for col in ["H.t","H.i","H.e","H.Shift.r","H.Return"]:
    sns.distplot(user_1[col], fit=norm, kde=False,color='red')
    sns.distplot(user_2[col], fit=norm, kde=False,color='blue')
    sns.distplot(user_3[col], fit=norm, kde=False,color='green')
    plt.figure()


# All the plots above show that there is a difference in the Gaussian models for the users. Some of keystrokes like "H.t","H.i","H.e","H.Shift.r","H.Return" show significant difference. To check if the differnce is only with the first three users or with all, plotting the Gaussian models for all the 50 users for "H.t","H.i","H.e","H.Shift.r","H.Return" 

# In[57]:

from scipy.stats import norm
for col in ["H.t","H.i","H.e","H.Shift.r","H.Return"]:
    for i in range (0,len(df),400):
        tmp=df[i:i+400]
        sns.distplot(tmp[col], fit=norm, kde=False)
    plt.figure()


# ### Gaussian models can be used to differentiate the users based on the typing pattern.
