import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My parents new healthy diner")
streamlit.header("Breakfast menu")
streamlit.text("🥣 Omega 3") 
streamlit.text("🥗 Kale")
streamlit.text("🐔 Hard-Boiled")
streamlit.text("🥑 🍞 Avacodo")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected  = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
  else:
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
  streamlit.error()
streamlit.write('The user entered ', fruit_choice)
streamlit.stop()

streamlit.header("The fruit load list contains:")

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
  my_cur.execute("select * from fruit_load_list")
  return my_cur.fetchall()

if streamlit.button("Get fruit load list")
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")

