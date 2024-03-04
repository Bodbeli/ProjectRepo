#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **SpaceX  Falcon 9 First Stage Landing Prediction**
# 

# ## Assignment: Exploring and Preparing Data
# 

# Estimated time needed: **70** minutes
# 

# In this assignment, we will predict if the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is due to the fact that SpaceX can reuse the first stage.
# 
# In this lab, you will perform Exploratory Data Analysis and Feature Engineering.
# 

# Falcon 9 first stage will land successfully
# 

# ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing_1.gif)
# 

# Several examples of an unsuccessful landing are shown here:
# 

# ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)
# 

# Most unsuccessful landings are planned. Space X performs a controlled landing in the oceans.
# 

# ## Objectives
# 
# Perform exploratory Data Analysis and Feature Engineering using `Pandas` and `Matplotlib`
# 
# *   Exploratory Data Analysis
# *   Preparing Data  Feature Engineering
# 

# ### Import Libraries and Define Auxiliary Functions
# 

# We will import the following libraries the lab
# 

# In[50]:


#import piplite
#await piplite.install(['numpy'])
#await piplite.install(['pandas'])
#await piplite.install(['seaborn'])


# In[1]:


# pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns


# In[ ]:


## Exploratory Data Analysis


# In[51]:


#from js import fetch
#import io


# First, let's read the SpaceX dataset into a Pandas dataframe and print its summary
# 

# In[52]:


#URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
#resp = await fetch(URL)
#dataset_part_2_csv = io.BytesIO((await resp.arrayBuffer()).to_py())
#df=pd.read_csv(dataset_part_2_csv)
#df.head(5)


# In[53]:


import os
import glob
import pandas as pd
#df = pd.read_csv(r"C:/Users/Zurab/Desktop/IBM Data Science Professional Certificate/Applied Data Science Capstone/dataset_part_2.csv")
df = pd.read_csv(r"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
df.head(5)


# First, let's try to see how the `FlightNumber` (indicating the continuous launch attempts.) and `Payload` variables would affect the launch outcome.
# 
# We can plot out the <code>FlightNumber</code> vs. <code>PayloadMass</code>and overlay the outcome of the launch. We see that as the flight number increases, the first stage is more likely to land successfully. The payload mass is also important; it seems the more massive the payload, the less likely the first stage will return.
# 

# In[4]:


sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()


# 7zWe see that different launch sites have different success rates.  <code>CCAFS LC-40</code>, has a success rate of 60 %, while  <code>KSC LC-39A</code> and <code>VAFB SLC 4E</code> has a success rate of 77%.
# 

# Next, let's drill down to each site visualize its detailed launch records.
# 

# In[20]:


### TASK 1: Visualize the relationship between Flight Number and Launch Site


# Use the function <code>catplot</code> to plot <code>FlightNumber</code> vs <code>LaunchSite</code>, set the  parameter <code>x</code>  parameter to <code>FlightNumber</code>,set the  <code>y</code> to <code>Launch Site</code> and set the parameter <code>hue</code> to <code>'class'</code>
# 

# In[5]:


# Plot a scatter point chart with x axis to be Flight Number and y axis to be the launch site, and hue to be the class value
sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("LaunchSite",fontsize=20)
plt.show()


# Now try to explain the patterns you found in the Flight Number vs. Launch Site scatter point plots.
# 

# In[6]:


x=df.PayloadMass
y=df.LaunchSite


# In[7]:


### TASK 2: Visualize the relationship between Payload and Launch Site
plt.scatter(x, y, marker='o')
plt.xlabel("PayloadMass")
plt.ylabel("LaunchSite")
plt.show()


# We also want to observe if there is any relationship between launch sites and their payload mass.
# 

# In[31]:


# Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value
sns.catplot(y="LaunchSite", x="PayloadMass", hue="Class", data=df, aspect = 5)
plt.xlabel("PayloadMass",fontsize=20)
plt.ylabel("LaunchSite",fontsize=20)
plt.show()


# Now if you observe Payload Vs. Launch Site scatter point chart you will find for the VAFB-SLC  launchsite there are no  rockets  launched for  heavypayload mass(greater than 10000).
# 

# In[ ]:


### TASK  3: Visualize the relationship between success rate of each orbit type


# Next, we want to visually check if there are any relationship between success rate and orbit type.
# 

# Let's create a `bar chart` for the sucess rate of each orbit
# 

# In[9]:


# HINT use groupby method on Orbit column and get the mean of Class column
df_bar=df.groupby('Orbit')['Class'].mean()
df_bar.values


# In[10]:


plt.bar(df_bar.index,df_bar.values)#
#plt.xlabel("FlightNum ber")
plt.ylabel("sucess rate")
plt.show()


# Analyze the ploted bar chart try to find which orbits have high sucess rate.
# 

# In[ ]:


### TASK  4: Visualize the relationship between FlightNumber and Orbit type


# For each orbit, we want to see if there is any relationship between FlightNumber and Orbit type.
# 

# In[11]:


# Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value
sns.catplot(y="Orbit", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()


# You should see that in the LEO orbit the Success appears related to the number of flights; on the other hand, there seems to be no relationship between flight number when in GTO orbit.
# 

# In[ ]:


### TASK  5: Visualize the relationship between Payload and Orbit type


# Similarly, we can plot the Payload vs. Orbit scatter point charts to reveal the relationship between Payload and Orbit type
# 

# In[12]:


# Plot a scatter point chart with x axis to be Payload and y axis to be the Orbit, and hue to be the class value
sns.catplot(y="Orbit", x="PayloadMass", hue="Class", data=df, aspect = 5)
plt.xlabel("Payload",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()


# With heavy payloads the successful landing or positive landing rate are more for Polar,LEO and ISS.
# 
# However for GTO we cannot distinguish this well as both positive landing rate and negative landing(unsuccessful mission) are both there here.
# 

# In[ ]:


### TASK  6: Visualize the launch success yearly trend


# You can plot a line chart with x axis to be <code>Year</code> and y axis to be average success rate, to get the average launch success trend.
# 

# The function will help you get the year from the date:
# 

# In[47]:


# A function to Extract years from the date 
year=[]
def Extract_year():
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year
Extract_year()
df['Date'] = year
df.head()
    


# In[54]:


# Plot a line chart with x axis to be the extracted year and y axis to be the success rate
df_line=df.groupby('Date')['Class'].mean()
plt.plot(df_line.index,df_line.values)
plt.ylabel("sucess rate")
plt.show()


# you can observe that the sucess rate since 2013 kept increasing till 2020
# 

# In[ ]:


## Features Engineering


# By now, you should obtain some preliminary insights about how each important variable would affect the success rate, we will select the features that will be used in success prediction in the future module.
# 

# In[13]:


features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()


# In[ ]:


### TASK  7: Create dummy variables to categorical columns


# Use the function <code>get_dummies</code> and <code>features</code> dataframe to apply OneHotEncoder to the column <code>Orbits</code>, <code>LaunchSite</code>, <code>LandingPad</code>, and <code>Serial</code>. Assign the value to the variable <code>features_one_hot</code>, display the results using the method head. Your result dataframe must include all features including the encoded ones.
# 

# In[29]:


# HINT: Use get_dummies() function on the categorical columns
features_one_hot=pd.get_dummies(features, columns=["Orbit","LaunchSite","LandingPad","Serial"])
features_one_hot.head()


# In[ ]:


### TASK  8: Cast all numeric columns to `float64`


# Now that our <code>features_one_hot</code> dataframe only contains numbers cast the entire dataframe to variable type <code>float64</code>
# 

# In[32]:


# HINT: use astype function
features_one_hot.dtypes


# In[49]:


for col in features_one_hot.columns:
    if features_one_hot[col].dtypes!= "bool":
        features_one_hot[[col]] = features_one_hot[[col]].astype("float64")
features_one_hot.dtypes


# We can now export it to a <b>CSV</b> for the next section,but to make the answers consistent, in the next lab we will provide data in a pre-selected date range.
# 

# <code>features_one_hot.to_csv('dataset_part\_3.csv', index=False)</code>
# 

# ## Authors
# 

# [Pratiksha Verma](https://www.linkedin.com/in/pratiksha-verma-6487561b1/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork865-2022-01-01)
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By      | Change Description      |
# | ----------------- | ------- | -------------   | ----------------------- |
# | 2022-11-09        | 1.0     | Pratiksha Verma | Converted initial version to Jupyterlite|
# 

# ### <h3 align="center"> IBM Corporation 2022. All rights reserved. <h3/>
# 
