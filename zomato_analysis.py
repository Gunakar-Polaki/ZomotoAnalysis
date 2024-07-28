import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
dataframe = pd.read_csv("Zomato data .csv")

# Function to handle rate column
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)

# Title of the application
st.title('Zomato Data Analysis')

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.multiselect(
    'Select analysis to perform:',
    ['Explore listed_in (type) column', 
     'Preferred by a larger number of individuals', 
     'Restaurant with maximum votes', 
     'Explore online_order column', 
     'Explore rate column']
)

# Explore listed_in (type) column
if 'Explore listed_in (type) column' in options:
    st.subheader('Explore by Type of Restaurant ')
    fig, ax = plt.subplots()
    sns.countplot(x=dataframe['listed_in(type)'], ax=ax)
    ax.set_xlabel("Type of restaurant")
    st.pyplot(fig)

# Preferred by a larger number of individuals
if 'Preferred by a larger number of individuals' in options:
    st.subheader('Preferred by a larger number of individuals')
    grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data})
    fig, ax = plt.subplots()
    ax.plot(result, c="green", marker="o")
    ax.set_xlabel("Type of restaurant", c="red", size=20)
    ax.set_ylabel("Votes", c="red", size=20)
    st.pyplot(fig)

# Restaurant with maximum votes
if 'Restaurant with maximum votes' in options:
    st.subheader('Restaurant with maximum votes')
    max_votes = dataframe['votes'].max()
    restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
    st.write("Restaurant(s) with the maximum votes:")
    st.write(restaurant_with_max_votes)

# Explore online_order column
if 'Explore online_order column' in options:
    st.subheader('Explore online orders ')
    fig, ax = plt.subplots()
    sns.countplot(x=dataframe['online_order'], ax=ax)
    st.pyplot(fig)

# Explore rate column
if 'Explore rate column' in options:
    st.subheader('Explore by ratings ')
    fig, ax = plt.subplots()
    ax.hist(dataframe['rate'], bins=5)
    ax.set_title("Ratings Distribution")
    st.pyplot(fig)

# Examine whether online orders receive higher ratings
if 'Compare online and offline order ratings' in options:
    st.subheader('Compare online and offline order ratings')
    fig, ax = plt.subplots()
    sns.boxplot(x='online_order', y='rate', data=dataframe, ax=ax)
    st.pyplot(fig)

# Heatmap for listed_in(type) and online_order
if 'Heatmap of listed_in(type) and online_order' in options:
    st.subheader('Heatmap of listed_in(type) and online_order')
    pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    fig, ax = plt.subplots()
    sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d', ax=ax)
    ax.set_title("Heatmap")
    ax.set_xlabel("Online Order")
    ax.set_ylabel("Listed In (Type)")
    st.pyplot(fig)
