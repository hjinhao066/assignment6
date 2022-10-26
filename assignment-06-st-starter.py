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
