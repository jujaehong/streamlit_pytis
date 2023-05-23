# 가상환경 통일 설정 ( 팀에 맞는 환경으로 맞추는 작업 )

# (base) C:\Users\jaehong\Documents\GitHub\streamlit_pytis> 아래 소스 붙여넣기

# conda create -n app_dash python=3.9 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn

# conda - 아나콘다 명령어
# create 가상환경 만들어라
# -n 다음에 나오는것은 가상환경의 이름
# 가상환경이름 : app_dash
# python=3.9 : 파이썬 3.9버전으로 해라
# pip install : openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn 인스톨해라

# conda activate app_dash ( app_ dash 로 진입 )
# conda deactivate ( app_ dash 에서 나가기 )
# python --version ( 버전 확인 )

# streamlit run app.py  ( streamlit 실행하는 명령어 )
# 서버를 끌때는 컨트로 + c

import streamlit as st

def main():
    st.title('내 앱 대시보드') # st. 화면에 제목을 넣을 때 시작 문구
    st.text('데이터 분석 앱 입니다.')
    st.text('테스트 앱입니다.')

if __name__ == '__main__' :
    main()

