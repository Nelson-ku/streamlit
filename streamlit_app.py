import streamlit as st
import pandas as pd
import numpy as np
st.header('st.button')

if st.button('say hello'):
    st.write('why hello there ')
else:
    st.write('Goodbye')



df=pd.DataFrame({
    'index':[1,2,3,4],
    'scores':[10,20,30,40]
})

df 

# used to draw a table of random values  Numpy to generate a random sample, and the st.dataframe() method to draw an interactive table.

dataframe=np.random.randn(10,20)
st.dataframe(dataframe)

 
st.write('highlighting data')
dataframe= pd.DataFrame(
    np.random.randn(10,20),
    columns=(' col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))#highlighting your table

#drawing another a table using the st.table() function
st.table(dataframe)


#drawing a line chart using st.line_chart() function
st.write('chart data')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']

 )

st.line_chart(chart_data)

st.write('plot a map using st.map() function of the san fransisco')

map_data=pd.DataFrame(
    np.random.randn(1000,2) /[50,50]+ [37.76, -122.4],
    columns=['lat','lon']
)

st.map(map_data)


st.write('working with widgets ')
st.write('this slider returns the squares of the number selected')


x= st.slider('x')# this is a widget
st.write(x, 'squared is', x * x)


#create an  input box 
st.text_input('your name', key='name')

st.session_state.name
 

#use a checkbox to display data in a table
if st.checkbox('show dataframe'):
    chart_data=pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    chart_data

#using a selectbox to choose from a series where you can write in the options you want, or pass through an array or data frame column
df=pd.DataFrame({
     'first column ':[1,2,3,4],
     'second  column':[10,20,30,40]
})

option =st.selectbox(
    'which number do you like best',
    df['first column']
)
'you selected :',option
