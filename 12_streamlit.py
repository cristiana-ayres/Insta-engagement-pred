import streamlit as st
import pandas as pd
from sklearn import linear_model

data = pd.read_csv("followers_top_final.csv")

# creating the logistic regression model
X = data[['engagement_activity','followers', 'following', 'total_posts', 'likes_per_post', 'comments_per_post']]
y = data['channel_associated_on_bio']

#  create the model 
logistic = linear_model.LogisticRegression()

# train the model 
logistic.fit(X,y)

st.title('This is our main title')
st.text('This is any text')


input_feature = st.text_input('How many followers do you have?') # featureX1
# input_feature = st.text_input('How many accounts are you following?') # featureX2
# input_feature = st.text_input('How many total posts do you have?') # featureX3
# input_feature = st.text_input('How many followers do you have?') # featureX4
# input_feature = st.text_input('How many followers do you have?') # featureX5
# input_feature = st.text_input('How many followers do you have?') # featureX6
# many inputs

button = st.button('predict something')

user_input = {'feat1':[input_feature], 'feat2': [input_feature]}
to_predict = pd.DataFrame(user_input)

if button:
    # prediction model
    try:
        result = logistic.predict(to_predict)
        if result == 0:
            st.write('Your engagement will be low')
        else:
            st.write('Your engagement will be high')
    except:
        st.write('Please input an integer')

print(input_feature)