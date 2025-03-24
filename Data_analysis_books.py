#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv (r"C:\Users\SHIVANSH SHARMA\Downloads\analysis\Books_Data_Clean.csv")


# In[6]:


df.head()


# In[7]:


df.describe()


# In[9]:


df = df[df["Publishing Year"] > 1900]


# In[10]:


df.describe()


# In[13]:


df.isna().sum() ## to get total no of missing values in dataset 


# In[12]:


df.dropna(subset = "Book Name", inplace = True) ## here we drop missing values in Book Name column and using inplace = True, we change/modify in original dataset


# In[15]:


df.duplicated().sum() ## count of duplicated rows


# In[16]:


df.nunique() ##The command df.nunique() in pandas is used to count the number of unique values in each column of a DataFrame.


# In[21]:


plt.hist(df["Publishing Year"])
plt.xlabel("Publishing Year")
plt.ylabel("Frequency")
plt.title(" Distribution of Publishing Year")
plt.show()


# In[23]:


df["genre"].value_counts().plot(kind = "bar")
plt.xlabel("Genre")
plt.ylabel("Number of Books")
plt.title("Number of books in each Genre")
plt.show()


# In[24]:


df.groupby("Author")["Book_average_rating"].mean() ####The command df.groupby("Author")["Book_average_rating"].mean() in pandas is used to calculate the average book rating per author


# In[27]:


sns.boxplot(x = "genre", y = "Book_ratings_count", data = df)
plt.xlabel("genre")
plt.ylabel("Book_ratings_count")
plt.title(" Box plot of book ratings count for each genre")
plt.show()


# In[28]:


language_counts = df["language_code"].value_counts()


# In[35]:


plt.pie(language_counts, labels = language_counts.index, startangle = 90, autopct= "%1.1f%%")
plt.title("language distirbution of books")
plt.show()


# In[41]:


df.groupby("Publisher ")["publisher revenue"].sum().sort_values(ascending = False)


# In[42]:


df.groupby("Author_Rating")["Book_ratings_count"].var() ####calculates the variance of book ratings count for each unique Author_Rating


# In[44]:


plt.scatter(df["Book_average_rating"], df["Book_ratings_count"])
plt.xlabel("Book Average Rating")
plt.ylabel("Book_ratings_count")
plt.title(" scatter plot of book average rating vs Book ratings count")
plt.show()


# In[48]:


df.groupby("Publishing Year")["units sold"].sum().plot(kind = "line", marker = "o")
plt.xlabel("Publishing year")
plt.ylabel("Total units sold")
plt.title("total units sold over the years")
plt.show()


# In[ ]:




