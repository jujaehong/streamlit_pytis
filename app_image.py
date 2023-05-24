import streamlit as st
from datetime import datetime
import os
import pandas as pd
from app_utils import save_uplpaded_file


def run_app_image() :
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