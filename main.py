import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from components import recommendations
import home


# Apply theme from the config file
st.set_page_config(
    page_title="Аналитика по городу",
    page_icon="🏙️",
    layout="centered",
    initial_sidebar_state="expanded"  # "expanded" collapsed
)

# Adding custom CSS styles using components.html
components.html("""
    <style>
    .container-xxl.d-flex.flex-column.flex-shrink-0.p-3 {
        width: 100%;
        background-color: #f8f9fa; /* Light gray background */
        padding: 20px; /* Add padding */
        border-radius: 10px; /* Rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow */
    }
    </style>
    """, height=0)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Create a sidebar option menu
        with st.sidebar:
            app = option_menu(
                menu_title='🏙️Аналитика по Туризму',
                options=['🖥️ Главная'],
                icons=['house-garden', 'house-garden', 'house-garden',
                       'house-garden', 'house-garden', 'house-garden',
                       'house-garden', 'house-garden'],
                menu_icon='house-garden',
                default_index=0,  # Change the default index to 0 for "🖥️ Главная"
                styles={
                    "container": {"padding": "5!important", "width": "100%"},  # Adjust width here
                    # "icon": {"color": "white", "font-size": "0px"},
                    "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "orange"},
                    "nav-link-selected": {"background-color": "#44484d"},
                }
            )

        # Display selected app based on user choice
        if app == "🖥️ Главная":
            recommendations.app()
        # elif app == "📚 Анализ по секторам":
        #     recommendations.app()
# Create an instance of MultiApp and add your apps
multi_app = MultiApp()

multi_app.add_app("Карта Туризма", recommendations.app)

# Run the MultiApp
multi_app.run()

