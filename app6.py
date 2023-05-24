import streamlit as st

def main():
   
    st.title('내 앱 대시보드') # st. 화면에 제목을 넣을 때 시작 문구
    name = st.text_input('이름을 입력하세요!',max_chars = 10) # max_chars = 글자수 제한
    st.text('입력하신 이름은' + name) 
    message = st.text_area('메세지를 입력하세요',height = 1) # text_area 메세지칸 만들기 height 높이제한
    st.text(message)

    # 숫자 입력 정수

    number = st.number_input('숫자를 입력하세요~',1,100,step = 10)
    st.text(number * 3)

    # 숫자 입력 실수

    number2 = st.number_input('숫자를 입력하세요~',1.0, 100.0)
    st.text(number2 * 3)

    # 날짜
    my_date = st.date_input ('약속 날짜 입력')
    print(my_date)
    print( type(my_date))

    # 시간
    my_time = st.time_input('시간 선택')
    print(type(my_time))
    st.text(my_time)

    # 비밀번호 처리방법
    password = st.text_input('비밀번호 입력', type = 'password')
    st.text(password)

    # 색 입력
    color = st.color_picker('색을 선택하세요')
    st.text(color)


if __name__ == '__main__' :
    main()