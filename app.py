import streamlit as st
import pickle
import pandas as pd


st.title("Food Recommender System")


food_list = pickle. load(open('Customer.pkl', 'rb'))
data = pd.DataFrame(food_list)
Breakfast_list = pickle. load(open('Breakfast.pkl', 'rb'))
Dinner_list = pickle. load(open('Dinner.pkl', 'rb'))
Lunch_list = pickle. load(open('Lunch.pkl', 'rb'))
# food_list1 = food_list['Breakfast'].values

selected_food = st.selectbox('What kind of food you like:?',
                             ('Breakfast','Lunch', 'Dinner'))

if selected_food is ('Breakfast'):

    def recommend(food):
        food_index = data[data['Breakfast'] == food].index[0]
        distances = Breakfast_list[food_index]
        food_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]

        recommended_foods = []
        for i in food_list:
            recommended_foods.append(data.iloc[i[0]].Breakfast)
        return recommended_foods
    selected_food = st.selectbox('What would you like to have?', data['Breakfast'].values)

    if st.button('Recommend'):
        recommendations = recommend(selected_food)
        st.subheader("You should also try this")
        for i in recommendations:
            st.write(i)

if selected_food is ('Lunch'):

    def recommend(food):
        food_index = data[data['Lunch'] == food].index[0]
        distances = Lunch_list[food_index]
        food_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:2]

        recommended_foods = []
        for i in food_list:
            recommended_foods.append(data.iloc[i[0]].Lunch)
        return recommended_foods
    selected_food = st.selectbox('What would you like to have?', data['Lunch'].values)

    if st.button('Recommend'):
        recommendations = recommend(selected_food)
        st.subheader("You should also try this")
        for i in recommendations:
            st.write(i)

if selected_food is ('Dinner'):
    def recommend(food):
        food_index = data[data['Dinner'] == food].index[0]
        distances = Dinner_list[food_index]
        food_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:2]

        recommended_foods = []
        for i in food_list:
            recommended_foods.append(data.iloc[i[0]].Dinner)
        return recommended_foods

    selected_food = st.selectbox('What would you like to have?', data['Dinner'].values)

    if st.button('Recommend'):
        recommendations = recommend(selected_food)
        st.subheader("You should also try this")
        for i in recommendations:
            st.write(i)

st.snow()




