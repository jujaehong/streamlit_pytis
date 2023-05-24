import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
   
    st.title('내 앱 대시보드') # st. 화면에 제목을 넣을 때 시작 문구
    df = pd.read_csv('data/iris.csv')

    st.dataframe(df)

    # sepal_length, sepal_width 의 관계를 차트로

    fig = plt.figure()
    plt.scatter(data = df, x = 'sepal_length' , y = 'sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.regplot(data = df, x = 'sepal_length' , y = 'sepal_width') 
    st.pyplot(fig2)

    correlation = df[['sepal_length','sepal_width']].corr() # 구글에서 상관분석 위키백과 참조
    st.dataframe(correlation)

    # sepal_length 로 히스토그램을 그린다.
    # bin 의 갯수는 10개로 

    fig3 = plt.figure(figsize= (10,4))
    plt.hist(data = df , x = 'sepal_length', rwidth=0.8 , bins= 10 )
    st.pyplot(fig3)

    plt.subplot(1, 2, 1)
    plt.hist(data = df , x = 'sepal_length', rwidth=0.8 , bins= 10 )
 
    plt.subplot(1, 2, 2)
    plt.hist(data = df , x = 'sepal_length', rwidth=0.8 , bins= 10 )

    st.pyplot(fig3)

    # species 컬럼에는 종에 대한 정보가 들어있는데,
    # 각 종별로 몇개씩의 데이터가 있는지
    # 차트로 나타내시오.

    st.dataframe(df['species'].value_counts())

    fig4 = plt.figure()
    sns.countplot(data=df, x='species')
    st.pyplot(fig4)

    #### 데이터프레임의 차트 그리는 코드도 실행 가능!
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='barh') #기본으로 선으로 표시 , 막대로 보기위해서는 kind='bar' 넣기 ,kind='bar'는 옆으로
    st.pyplot(fig5)

    
    # 데이터프레임 자체 plot 함수는 스트림릿에서 안된다.
    # fig6 = plt.figure()
    # df.plot()
    # st.pyplot(fig6)

    fig7 = plt.figure()
    df['sepal_length'].hist(bins=70)
    st.pyplot(fig7)





if __name__ == '__main__' :
    main()