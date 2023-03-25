import streamlit as st
import pandas as pd
import numpy as np
import ydata_profiling
from datetime import datetime, time
from streamlit_pandas_profiling import st_profile_report


st.title('This is My First Streamlit App!')
st.write('Welcome to there!')

# 1.slider
st.header('st.slider')

# Example 1
age = st.slider('How old are you?', 0, 130, 25)
st.write(f'I am {age} years old!')

# Example 2
st.subheader('Range slider')
values = st.slider('Select a range of values',
                   0.0, 100.0, (25.0, 75.0)
                   )
st.write(f'Values: {values}')

# Example 2
st.subheader('Range time slider')
appointment = st.slider("Schedule your appointment:",
                        min_value=time(0, 0),
                        max_value=time(15, 0),
                        value=(time(11, 30), time(12, 45))
                        )
st.write(f'You are scheduled '
         f'for: {(str(appointment[0].hour) + "."+ str(appointment[0].minute), str(appointment[1].hour) + "."+ str(appointment[1].minute))}')

# Example 4
st.subheader('Datetime slider')
start_time = st.slider("When do you start?",
                       value=datetime(2023, 1, 1, 9, 30),
                       format="YYYY-MM-DDThh:mm")
st.write("Start time:", start_time)


# 2.line_chart
st.header('Line chart')

chart_data = pd.DataFrame(np.random.randn(20, 3),
                          columns=['a', 'b', 'c']
                          )
st.line_chart(chart_data)


# 3.selectbox
st.header('st.selectbox')
option = st.selectbox('What is your favorite color?',
                      ('Blue', 'Red', 'Green'))
st.write('Your favorite color is ', option)

# 4.multiselect
st.header('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue']
    )

# 5.checkbox
st.header('st.checkbox')
st.write('what would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
if icecream:
    st.write('Great! Here is some more Icecream')
if coffee:
    st.write('Okay! Here is some more Coffee')
if cola:
    st.write('Here you go cola')


# 6.第三方模块：streamlit_pandas_profiling
st.header('`streamlit_pandas_profiling`')
df = pd.read_csv('data/penguins_cleaned.csv')
pr = df.profile_report()
st_profile_report(pr)
