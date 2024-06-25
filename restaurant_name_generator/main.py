import streamlit as st
from langchain_model import generate_restaurant_name_and_items

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Brazilian", "Thai", "Indo-Chinese", "Korean"))
food_type = st.sidebar.radio("What type of restaurant do you want?", ["Vegetarian", "Non-Vegetarian", "Vegan"])

if st.sidebar.button("Generate", type = "primary"):
    response = generate_restaurant_name_and_items(cuisine, food_type)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")

    st.write("**Menu Items:**")
    for item in menu_items:
        st.write("-", item)