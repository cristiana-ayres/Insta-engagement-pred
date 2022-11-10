import streamlit as st
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("followers_all_final.csv")

# creating the logistic regression model
X = data[['followers', 'following', 'total_posts', 'time_on_app_years', 'likes_per_post', 'comments_per_post', 'engagement_activity']]
y = data['engagement_type']

# create the scaler 
scaler = StandardScaler()

# fit our data to the standard scaler 
scaler.fit(X)

# transform the data
scaler.transform(X)

scaled_X = pd.DataFrame(scaler.transform(X), columns=X.columns)

#  create the model 
logistic = linear_model.LogisticRegression()

# train the model 
logistic.fit(scaled_X,y)

st.title('This is our main title')
st.text('This is any text, describing our app')

# inputs
input_feature1 = int(st.number_input('How many followers do you have?')) # featureX1
input_feature2 = int(st.number_input('How many accounts are you following?')) # featureX2
input_feature3 = int(st.number_input('How many total posts do you have?')) # featureX3
input_feature4 = int(st.number_input('When was your first post?')) # featureX4
input_feature5 = int(st.number_input('How many likes do you have on your last 3 posts in total?')) # featureX5
input_feature6 = int(st.number_input('How many comments do you have on your last 3 posts in total?')) # featureX6


button = st.button('Start prediction')

user_input = {'followers':[input_feature1], 'following': [input_feature2], 'total_posts': [input_feature3], 'time_on_app_years': [input_feature4], 'likes_per_post': [input_feature5], 'comments_per_post': [input_feature6]}
to_predict = pd.DataFrame(user_input)

to_predict['engagement_activity'] = ((input_feature5 + input_feature6) * 100 / input_feature1)



# # fit our data to the standard scaler 
# scaler.fit(to_predict)

# transform the data
scaler.transform(to_predict)

scaled_X_new = pd.DataFrame(scaler.transform(to_predict), columns=to_predict.columns)



if button:
    # prediction model
    try:
        result = logistic.predict(scaled_X_new)
        if result == "Low Engagement":
            st.write('Your engagement will be low')
        else:
            st.write('Your engagement will be high')
    except:
        st.write('Please input an integer')

