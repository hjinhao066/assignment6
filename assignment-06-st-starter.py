# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
# show the title
st.title('Titanic app by Jinhao Hu')

# read csv and show the dataframe
df = pd.read_csv('train.csv')

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig,ax=plt.subplots(1,3,figsize=(15,5))
df1=df[(df['Pclass']==1)]
df2=df[(df['Pclass']==2)]
df3=df[(df['Pclass']==3)]

df1.Fare.plot.box(ax=ax[0])
df2.Fare.plot.box(ax=ax[1])
df3.Fare.plot.box(ax=ax[2])
ax[0].set_xlabel('PClass = 1')
ax[1].set_xlabel('PClass = 2')
ax[2].set_xlabel('PClass = 3')  
ax[0].set_ylabel('Fare')
