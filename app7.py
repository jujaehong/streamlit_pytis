import streamlit as st

from datetime import datetime

import os

import pandas as pd

# streamlit run app7.py
# 디렉토리 이름과, 파일이름을 주면,
# 해당 디렉토리에 파일을 저장해주는 함수
def save_uplpaded_file(directory, file) :
    # 1. 저장할 디렉토리가 있는지 확인하고,
    #    없으면 디렉토리를 먼저 만든다.
    if not os.path.exists(directory) : # 이 디렉토리가 있니? 없다면
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일저장
    with open(os.path.join(directory, file.name),'wb') as f :
        f.write(file.getbuffer())
    return st.success('파일 저장 완료')



def main():
   
    st.title('내 앱 대시보드') # st. 화면에 제목을 넣을 때 시작 문구

    menu = ['이미지업로드', 'csv업로드', 'About']
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == menu[0] :
        st.subheader('이미지 파일 업로드')

        img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png','jpg','jpeg'])
        if img_file is not None :

            print(type(img_file)) 
            print(img_file.name) # 파일명
            print(img_file.size) # 파일크기
            print(img_file.type) # 파일의 타입

            # 유저가 올린 파일을,
            # 서버에서 유니크하게 처리하기 위해서
            # 파일명을 현재시간 조합으로 해서 만든다.

            current_time = datetime.now()    
            print(current_time)  # 현재 시간
            print(current_time.isoformat().replace(':','_') + '.jpg') # 세계표준 시간  , replace(':','_')사용해서 콜론을 언더바로 바꾸기  
            filename = current_time.isoformat().replace(':','_') + '.jpg'    

            img_file.name = filename

            save_uplpaded_file('image', img_file)

            st.image('image/'+filename)



    elif choice == menu[1] :
        st.subheader('csv 파일 업로드')

        csv_file = st.file_uploader('CSV 파일 선택', type=['csv'])
        if csv_file is not None :
            current_time = datetime.now()
            filename = current_time.isoformat().replace(':','_')+'.csv'
            csv_file.name = filename
            save_uplpaded_file('csv' ,csv_file)
            df = pd.read_csv('csv/'+filename)
            st.dataframe(df)
   


        
    else :
        st.subheader('이 대시보드 설명')












if __name__ == '__main__' :
    main()