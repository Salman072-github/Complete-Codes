# %% [markdown]
# > # **Simple Linear Regression using Python**
# + ## Predicting Salary using Experience data
# + ## Total 11_steps

# %% [markdown]
# > ### 01_step Importing libraries

# %%
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

# %% [markdown]
# > ### 02_step Loading Data

# %%
df = pd.read_csv("salary_data.csv")
df.head()

# %% [markdown]
# > ### 03_step Checcking Numll values 

# %%
df.isnull().sum()

# %% [markdown]
# > ### 05_Spliting Data

# %%
X = df[["YearsExperience"]]
y = df["Salary"]

# %% [markdown]
# > ### 06_step  Importing sciket-learn

# %%
pip install scikit-learn

# %%
import sklearn

# %% [markdown]
# > ### 07_step model selection 

# %%
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=0)

# %% [markdown]
# > ### 08_step Impoting Linearregression

# %%

from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X_train,y_train)
model

# %%
model.predict(X_test)

# %% [markdown]
# > ### 09_step Visualization of train and test data

# %%

plt.scatter(X_train, y_train)
plt.plot(X_train, model.predict(X_train), color= "Black")
plt.title("Train data Plot")
plt.xlabel("Experience data of train data")
plt.ylabel("Salary data of train data")
plt.show()

# %%
from turtle import color


plt.scatter(X_test, y_test)
plt.plot(X_test, model.predict(X_test), color= "Red")
plt.title("test data plot")
plt.xlabel("Experience data")
plt.ylabel("Salary data")
plt.show()

# %% [markdown]
# > ### 10_step Checking fitness of your model

# %%
model.score(X_train, y_train)

# %%
model.score(X_test, y_test)

# %% [markdown]
# > ### 11_step Predicting Values using your model

# %%
model.predict(X_test)

# %%
model.predict([[3]])


