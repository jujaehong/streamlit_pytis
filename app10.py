import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

def main():
   
    st.title('내 앱 대시보드') # st. 화면에 제목을 넣을 때 시작 문구
    df1 = pd.read_csv('data/lang_data.csv')
    
    st.dataframe(df1)
    
    st.text(df1.shape)
   
    print(df1.columns[1:])
   
    lang_list = df1.columns[1:]
    
    choice_list =  st.multiselect('언어를 선택하세요', lang_list)
    
    print(choice_list)

    # 유저가 아무것도 선택 안했을때 처리 , 즉 비어있는 리스트임
    if len(choice_list) > 0 :
    

        choice_df = df1[choice_list]
        st.dataframe(choice_df) # 선택한 컬럼으로 데이터프레임을 가져온다.

        # 스트림릿이 제공하는 라인차트
        st.line_chart(choice_df)
        # 스트림릿이 제공하는 영역차트
        st.area_chart(choice_df)
            
    df2 = pd.read_csv('data/iris.csv')
    print(df2)

    # 스트림릿이 제공하는 바차트
    df3 = df2[['sepal_length','sepal_width']]
    st.bar_chart(df3)

    #  Altair 이용
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
    )

    st.altair_chart(chart)    
    
    ## 스트림릿의 map 차트 
    df4 = pd.read_csv('data/location.csv', index_col=0)
    print(df4)
    st.map(df4, 7)


       
    df5 = pd.read_csv('data/prog_languages_data.csv', index_col=0)
    st.dataframe(df5)
    
    # plotly 의 pie 차트(파이차트는 비율을 보고 싶을때)

    fig1 = px.pie(df5,'lang', 'Sum', title= '각 언어 비율')

    st.plotly_chart(fig1)

    # plotly 의 bar 차트

    df6 = df5.sort_values('Sum', ascending=False)

    fig2 = px.bar(df6, x = 'lang', y='Sum')

    st.plotly_chart(fig2)



if __name__ == '__main__' :
    main()  