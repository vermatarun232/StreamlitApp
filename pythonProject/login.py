import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('Loving it!')

st.write('This is a  normal text')

st.markdown("""
   ### My favourite movies
   - Race
   - Humshakals
   - Housefull
""")

st.code('''
    def foo(input):
        return input**2
    x=f(2)
''')

st.latex("""
        x^2+y^2=4

""")

df = pd.DataFrame({
    "name": ['Nitish', 'Ankit', 'Anupam'],
    "marks": [50, 60, 70],
    "package": [10, 12, 14]
})

df = pd.read_csv(r"E:\Downloads\flights.csv")
st.dataframe(df)

st.metric("Revenue", "Rs 3L", "-%3")

st.json({
    "name": ['Nitish', 'Ankit', 'Anupam'],
    "marks": [50, 60, 70],
    "package": [10, 12, 14]
})

st.image("https://rb.gy/h3cy5g")

st.video("Streamlit.mkv")

st.sidebar.title('Sidebar')

# Displaying images columnwise
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://rb.gy/h3cy5g")
with col2:
    st.image("https://rb.gy/h3cy5g")
with col3:
    st.image("https://rb.gy/h3cy5g")

st.error('Login Failed')
st.success('Login Successful')
st.info('Login Successful')
st.warning('Login Failed')

# Progress Bar
bar = st.progress(0)
for i in range(1, 101):
    time.sleep(0.01)
    bar.progress(i)

st.text_input("Enter Your Name")
st.number_input("Enter your age")
st.date_input("Enter registration date")
st.time_input("Current time")


# Button
email=st.text_input('Enter email')
password=st.text_input('Enter password')
gender=st.selectbox('Select sender',['Male','Female','Others'])
btn=st.button('Login')

if btn:
    if email=='tarun@gmail.com' and password=='1234':
        st.success('Login Successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')

# File Upload
import streamlit as st
import pandas as pd
file=st.file_uploader("Choose a file")
if file !=None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())


