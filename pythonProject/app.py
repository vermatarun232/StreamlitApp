import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title='Startup Analysis')

# df = pd.read_csv("startup_cleaned.csv",encoding="utf-8")

# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))
# Construct the full path to the CSV file
csv_path = os.path.join(dir_path, 'startup_cleaned.csv')

df = pd.read_csv(csv_path)
st.write("Files in directory:", os.listdir(os.getcwd()))

st.write("Current working directory:", os.getcwd())


# df['date'] = pd.to_datetime(df['date'], errors='coerce')
# df['year']=df['date'].dt.year
# df['month']=df['date'].dt.month
#
# def load_overall_analysis():
#     st.title('Overall Analysis')
#     #total invested amount
#     total = round(df['amount'].sum())
#     #max amount infused in a startup
#     max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
#     # avg ticket size
#     avg_funding=round(df.groupby('startup')['amount'].sum().mean())
#     # total funded startup
#     num_startups=df['startup'].nunique()
#     col1,col2,col3,col4 = st.columns(4)
#     with col1:
#         st.metric('Total', str(total) + ' Cr')
#     with col2:
#         st.metric('Max', str(max_funding) + ' Cr')
#     with col3:
#         st.metric('Avg', str(avg_funding) + ' Cr')
#     with col4:
#         st.metric('Funded startups', str(num_startups))
#
#     selected_mom=st.selectbox('MOM',['Total Amount','Startup'])
#     if(selected_mom=='Total Amount'):
#         st.subheader('MOM Total Amount Invested')
#         temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
#         temp_df['x-axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)
#         fig, ax = plt.subplots()
#         ax.plot(temp_df['x-axis'],temp_df['amount'])
#         ax.set_xlabel('Month-Year')
#         ax.set_ylabel('Amount')
#         st.pyplot(fig)
#     elif(selected_mom=='Startup'):
#         st.subheader('MOM Invested Startup')
#         temp_df = df.groupby(['year', 'month'])['amount'].nunique().reset_index()
#         temp_df['x-axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)
#         fig, ax = plt.subplots()
#         ax.plot(temp_df['x-axis'], temp_df['amount'])
#         ax.set_xlabel('Month-Year')
#         ax.set_ylabel('Startup')
#         st.pyplot(fig)
#     selected_input=st.selectbox('Pie',['Total','Count'])
#     if(selected_input=='Count'):
#         count=df.groupby('vertical')['startup'].nunique().sort_values(ascending=False)
#         fig, ax = plt.subplots()
#         ax.pie(count,labels=count.index)
#         st.pyplot(fig)
#     else:
#         sum = df.groupby('vertical')['amount'].sum().sort_values(ascending=False)
#         fig, ax = plt.subplots()
#         ax.pie(sum, labels=sum.index)
#         st.pyplot(fig)
#
#
# def load_investor_details(investor):
#     st.title(investor)
#     # Load the recent 5 investments of the investor
#     last5_df = df[df['investor'].str.contains(investor)].head()[['date', 'startup',
#                                                                  'vertical', 'city',
#                                                                  'round', 'amount']]
#     st.subheader('Most Recent Investments')
#     st.dataframe(last5_df)
#
#     col1, col2 = st.columns(2)
#     with col1:
#         # Biggest investments
#         big_series = (df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().
#                       sort_values(ascending=False)).head()
#         st.subheader('Biggest Investments')
#         fig, ax = plt.subplots()
#         ax.bar(big_series.index, big_series.values)
#         st.pyplot(fig)
#         # st.dataframe(big_df)
#     with col2:
#         vertical_series = df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum()
#         st.subheader('Sectors invested in')
#         fig1, ax1 = plt.subplots()
#         ax1.pie(vertical_series, labels=vertical_series.index, autopct='%0.01f%%')
#         st.pyplot(fig1)
#
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader('Stages invested in')
#         round_series = df[df['investor'].str.contains(investor)].groupby('round')['amount'].sum()
#         fig2, ax2 = plt.subplots()
#         ax2.pie(round_series, labels=round_series.index, autopct='%0.01f%%')
#         st.pyplot(fig2)
#     with col2:
#         st.subheader('Cities invested in')
#         cities_series = df[df['investor'].str.contains(investor)].groupby('city')['amount'].sum()
#         fig3, ax3 = plt.subplots()
#         ax3.pie(cities_series, labels=cities_series.index, autopct='%0.01f%%')
#         st.pyplot(fig3)
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader('YOY Investments')
#         df['year'] = df['date'].dt.year
#         YOY = df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()
#         fig4, ax4 = plt.subplots()
#         ax4.plot(YOY)
#         st.pyplot(fig4)
#     with col2:
#         st.subheader('Similar Investors')  #On the basis of invested together
#         # st.dataframe(sorted(set(df[df['investor'].str.contains(investor)]['investor'].str.split(',').sum()))[:10],column_config={'value':'investor'})
#         ls = sorted(set(df[df['investor'].str.contains(investor)]['vertical']))
#         st.dataframe(df[df['vertical'].isin(ls)][['vertical', 'investor']].head(10))  # On the basis of same sectors
#
#
# # Data Cleaning
# df['investor'].fillna('Undisclosed', inplace=True)
# st.sidebar.title('Startup Funding Analysis')
# option = st.sidebar.selectbox("Select one", ['Overall Analysis', 'Startup', 'Investor'])
#
# if option == 'Overall Analysis':
#     # st.title('Overall Analysis')
#     btn0 = st.sidebar.button('Show overall analysis')
#     if btn0:
#         pass
#     load_overall_analysis()
#
# elif option == 'Startup':
#     st.title('Startup Analysis')
#     st.sidebar.selectbox("Select startup", sorted(df['startup'].unique().tolist()))
#     btn1 = st.sidebar.button('Submit')
# else:
#     # st.title('Investor Analysis')
#     selected_investor = st.sidebar.selectbox("Select investor", sorted(set(df['investor'].str.split(',').sum())))
#     btn2 = st.sidebar.button('Show investor details')
#     if btn2:
#         load_investor_details(selected_investor)
