import streamlit as st
import pandas as pd
import numpy as np

st.title('A convenient tool for planning labor costs')
st.image("https://lh3.google.com/u/0/d/1N_hl7gRTc_IBeoVc0lbgnXzsbkoNtMX1=w1318-h644-iv1")
st.header('This version is only a demonostrate, the results are not reliable')
st.divider()
st.sidebar.header('Information about the employee')
experience = st.sidebar.number_input('Working experince',0,100)
department = st.sidebar.selectbox('Department',['АСО','ВиВ','ОВиК'])
building = st.sidebar.selectbox("Projecting building",["Аэротенк","Камера сбора осадка","Буферный резервуар","Здание решеток","Воздуходувная станция","Отстойник","Резервуар-усреднитель","НСВИ","Цех обработки осадка","АБК","Мехочистка","Реагентное хозяйство ФК"])

st.header('Projectiong data')
st.text('Inputs for the calculations of labor costs')
col1,col2, col3, col4 = st.columns(4)
df1 = pd.DataFrame({'А4':[col1.number_input('А4 Sheets',0,100)],
                    'A3':[col2.number_input('А3 Sheets',0,100)],
                    'A2':[col3.number_input('А2 Sheets',0,100)],
                    'A1':[col4.number_input('А1 Sheets',0,100)]
                    })

st.text('Check your data')
df = pd.DataFrame({'Experience':[experience],'Department':[department],"Building":[building]})

X_not_edited = pd.concat([df,df1], sort=False, axis =1)
st.data_editor(df1,num_rows=1)
st.data_editor(X_not_edited,num_rows=1)

departmentID = pd.DataFrame({"Department":["АСО","ВиВ","ОВиК"],
                             "Value":[0.6,0.08,0.11]})
buildingID = pd.DataFrame({"Building":["Аэротенк","Камера сбора осадка","Буферный резервуар","Здание решеток","Воздуходувная станция","Отстойник","Резервуар-усреднитель","НСВИ","Цех обработки осадка","АБК","Мехочистка","Реагентное хозяйство ФК"],
                           "Difficulty":[.05,.01,.01,.1,.12,.02,.01,.07,.32,.1,.07,.1]})

dep = departmentID["Value"].iloc[int(departmentID[departmentID["Department"]==department].index[0])]

bui = buildingID["Difficulty"].iloc[int(buildingID[buildingID["Building"]==building].index[0])]


df_edited = pd.DataFrame({"Building":[bui],'Department':[dep],'Experience':[experience],})
X_test = pd.concat([df_edited,df1], sort=False, axis =1)
st.data_editor(X_test,num_rows=1)

model = pd.read_pickle('https://github.com/Malassalive/Bachelor-s-thesis/raw/main/model%20(3).pickle')


st.divider()

st.header('Теперь нажимайте на кнопку ниже!')
st.text('A fortuneteller button')
if (st.button('Answer')):
    st.text('We recieved')
    st.dataframe(X_test)
    st.image('https://lh3.google.com/u/0/d/1vCK2EGGMMLtszAl7FpBJNbqaSEok0zDc=w1318-h644') 
    st.divider()
    answer = str(model.predict(X_test).round(0))
    st.write('The projecting process will take approximately', answer, ' hours')
    st.header(answer)
    
    

