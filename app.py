# import streamlit as st
# from components import home, land_prediction, strategy, methodology, about, recommendations, taxes, social
# # from pages import home, page1, page2

# # Установка конфигурации страницы
# st.set_page_config(
#     page_title="Аналитика по городу",
#     page_icon="🏙️",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Инициализация session state для управления текущей страницей
# if 'current_page' not in st.session_state:
#     st.session_state.current_page = "Главная"

# # Функция для отображения текущей страницы
# def show_page(page_name):
#     if page_name == "Главная":
#         home.app()
#     elif page_name == "Безопасность":
#         social.app()
#     elif page_name == "Бизнес":
#         land_prediction.app()
#     elif page_name == "Благоустройство":
#         strategy.app()
#     elif page_name == "Участки реновации":
#         recommendations.app()
#     elif page_name == "Социальные объекты":
#         taxes.app()
#     elif page_name == "Стоимость земли":
#         land_prediction.app()
#     elif page_name == "Налоги":
#         taxes.app()
#     elif page_name == "Развитие":
#         strategy.app()

# # Основная логика приложения
# def app():
#     show_page(st.session_state.current_page)

# if __name__ == "__main__":
#     app()
###############################################################################################

# import streamlit as st
# from pages import home, page1, page2

# # Установка конфигурации страницы
# st.set_page_config(
#     page_title="Аналитика по городу",
#     page_icon="🏙️",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Инициализация session state для управления текущей страницей
# if 'current_page' not in st.session_state:
#     st.session_state.current_page = "Home"

# # Функция для отображения текущей страницы
# def show_page(page_name):
#     if page_name == "Home":
#         home.app()
#     elif page_name == "Page1":
#         page1.app()
#     elif page_name == "Page2":
#         page2.app()

# # Основная логика приложения
# def app():
#     show_page(st.session_state.current_page)

# if __name__ == "__main__":
#     app()
####################################################################
# import streamlit as st
# from components import home, land_prediction, strategy, methodology, about, recommendations, taxes, social

# # Set page configuration
# st.set_page_config(
#     page_title="Аналитика по городу",
#     page_icon="🏙️",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Initialize session state for managing the current page
# if 'current_page' not in st.session_state:
#     st.session_state.current_page = "home"

# # Function to display the current page
# def show_page(page_name):
#     if page_name == "home":
#         home.app()
#     elif page_name == "land_prediction":
#         land_prediction.app()
#     elif page_name == "strategy":
#         strategy.app()
#     elif page_name == "methodology":
#         methodology.app()
#     elif page_name == "about":
#         about.app()
#     elif page_name == "recommendations":
#         recommendations.app()
#     elif page_name == "taxes":
#         taxes.app()
#     elif page_name == "social":
#         social.app()

# # Main logic of the application
# def app():
#     query_params = st.query_params
#     if 'page' in query_params:
#         st.session_state.current_page = query_params['page'][0]
#     show_page(st.session_state.current_page)

# if __name__ == "__main__":
#     app()


import streamlit as st

# Define page functions
def home_page():
    st.title("Главная")
    st.write("Добро пожаловать на главную страницу.")
    if st.button("Перейти к странице анализа"):
        st.session_state.page = "analysis"
    if st.button("Перейти к странице статистики"):
        st.session_state.page = "statistics"

def analysis_page():
    st.title("Анализ")
    st.write("Это страница анализа.")
    if st.button("Вернуться на главную"):
        st.session_state.page = "home"

def statistics_page():
    st.title("Статистика")
    st.write("Это страница статистики.")
    if st.button("Вернуться на главную"):
        st.session_state.page = "home"

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Render the current page
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "analysis":
    analysis_page()
elif st.session_state.page == "statistics":
    statistics_page()
