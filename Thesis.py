import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats

st.title('Удобный инструмент для планирования трудоемкости')
st.image("https://lh3.google.com/u/0/d/1N_hl7gRTc_IBeoVc0lbgnXzsbkoNtMX1=w1318-h644-iv1")
st.header('Данная версия является ознакомительной и больше похожа на генератор случайных чисел')
st.divider()
st.sidebar.header('Данные об исполнителе')
experience = st.sidebar.number_input('Стаж в годах',0,100)
department = st.sidebar.selectbox('Отдел',['АСО','ВиВ','ОВиК'])
building = st.sidebar.selectbox("Сооружение",["Аэротенк","Камера сбора осадка","Буферный резервуар","Здание решеток","Воздуходувная станция","Отстойник","Резервуар-усреднитель","НСВИ","Цех обработки осадка","АБК","Мехочистка","Реагентное хозяйство ФК"])

st.header('Информация о проектируемом разделе')
st.text('Введите основные вводные данные для расчета трудоемкости')
col1,col2, col3, col4 = st.columns(4)
df1 = pd.DataFrame({'А4':[col1.number_input('Количество листов А4',0,100)],
                    'A3':[col2.number_input('Количество листов А3',0,100)],
                    'A2':[col3.number_input('Количество листов А2',0,100)],
                    'A1':[col4.number_input('Количество листов А1',0,100)]
                    })

st.text('Проверьте введенные данные')
df = pd.DataFrame({'Стаж':[experience],'Отдел':[department],"Сооружение":[building]})

X_not_edited = pd.concat([df,df1], sort=False, axis =1)
st.data_editor(df1,num_rows=1)
st.data_editor(X_not_edited,num_rows=1)

departmentID = pd.DataFrame({"Отдел":["АСО","ВиВ","ОВиК"],
                             "Значение":[0.6,0.08,0.11]})
buildingID = pd.DataFrame({"Сооружение":["Аэротенк","Камера сбора осадка","Буферный резервуар","Здание решеток","Воздуходувная станция","Отстойник","Резервуар-усреднитель","НСВИ","Цех обработки осадка","АБК","Мехочистка","Реагентное хозяйство ФК"],
                           "Сложность":[.05,.01,.01,.1,.12,.02,.01,.07,.32,.1,.07,.1]})

dep = departmentID["Значение"].iloc[int(departmentID[departmentID["Отдел"]==department].index[0])]

bui = buildingID["Сложность"].iloc[int(buildingID[buildingID["Сооружение"]==building].index[0])]


df_edited = pd.DataFrame({"Строение":[bui],'Отдел':[dep],'Стаж':[experience],})
X_test = pd.concat([df_edited,df1], sort=False, axis =1)
st.data_editor(X_test,num_rows=1)

model = pd.read_pickle('https://github.com/Malassalive/Bachelor-s-thesis/raw/main/model%20(3).pickle')

import time

st.divider()

st.header('Теперь нажимайте на кнопку ниже!')
st.text('Загляните в свое будущее')
if (st.button('Узнать ответ')):
    st.text('Полученные нами данные')
    st.dataframe(X_test)
    st.image('https://lh3.google.com/u/0/d/1vCK2EGGMMLtszAl7FpBJNbqaSEok0zDc=w1318-h644') 
    time.sleep(5)
    st.divider()
    answer = str(model.predict(X_test).round(0))
    st.write('Проектирование приблизительно займет', answer, ' часа')
    st.header(answer)
    
    

