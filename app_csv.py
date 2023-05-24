import streamlit as st
from datetime import datetime
import os
import pandas as pd
from app_utils import save_uplpaded_file



def run_app_csv() :
    st.subheader('csv 파일 업로드')

    csv_file = st.file_uploader('CSV 파일 선택', type=['csv'])
    if csv_file is not None :
        current_time = datetime.now()
        filename = current_time.isoformat().replace(':','_')+'.csv'
        csv_file.name = filename
        save_uplpaded_file('csv' ,csv_file)
        df = pd.read_csv('csv/'+filename)
        st.dataframe(df)