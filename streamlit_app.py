import requests
import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')
# streamlit.header('Breakfast Menu') COPY THESE:    🥑🍞
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Pick some fruits', my_fruit_list.index, ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)



fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

streamlit.header('Fruityvice Fruit Advice!')
streamlit.dataframe(fruityvice_normalized)
