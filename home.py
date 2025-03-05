import streamlit as st
import base64
import random
import streamlit.components.v1 as components

def app():
    # Load background image
    with open("img/background.jpeg", "rb") as image_file:
        encoded_background = base64.b64encode(image_file.read()).decode()

    page_element = """
    <style>
    [data-testid="stAppViewContainer"]{
        background-image: url("https://i.ibb.co/6FtJ89T/banner-urban.png");
        background-size: cover;
    }
    [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"]{
        right: 2rem;
        background-image: url("https://cdn.iconscout.com/icon/free/png-256/hamburger-menu-462145.png");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

    # Define images for buttons and links
    buttons = {
        "Безопасность": {"image": "img/безопасность.png", "page": "pages/land_prediction.py", "tooltip": "Анализ безопасности городских районов"},
        "Бизнес": {"image": "img/финансы.png", "page": "pages/strategy.py", "tooltip": "Анализ бизнес активности"},
        "Благоустройство": {"image": "img/Благоустройство.png", "page": "pages/methodology.py", "tooltip": "Анализ благоустройства города"},
        "Участки реновации": {"image": "img/Экономика.png", "page": "pages/about.py", "tooltip": "Анализ участков реновации"},
        "Социальные объекты": {"image": "img/безопасность.png", "page": "pages/recommendations.py", "tooltip": "Анализ социальных объектов"},
        "Стоимость земли": {"image": "img/финансы.png", "page": "pages/taxes.py", "tooltip": "Анализ стоимости земли"},
        "Налоги": {"image": "img/Благоустройство.png", "page": "pages/social.py", "tooltip": "Анализ налоговой нагрузки"},
    }

    encoded_images = {}
    for name, info in buttons.items():
        with open(info["image"], "rb") as image_file:
            encoded_images[name] = base64.b64encode(image_file.read()).decode()

    # Function to check for button collisions
    def check_collision(x, y, positions, size=100, padding=10):
        for px, py in positions:
            if (x < px + size + padding and x + size + padding > px and
                y < py + size + padding and y + size + padding > py):
                return True
        return False

    # Generate random positions without collisions
    positions = []
    for _ in range(len(buttons)):
        while True:
            random_x = random.randint(150, 450)
            random_y = random.randint(0, 600)
            if not check_collision(random_x, random_y, positions):
                positions.append((random_x, random_y))
                break

    # Generate styles for animations
    keyframes_styles = ""
    for index in range(len(buttons)):
        keyframes_styles += f"""
        @keyframes move{index} {{
            0% {{ transform: translate(0, 0); }}
            25% {{ transform: translate({random.randint(-100, 100)}px, {random.randint(-100, 100)}px); }}
            50% {{ transform: translate({random.randint(-100, 100)}px, {random.randint(-100, 100)}px); }}
            75% {{ transform: translate({random.randint(-100, 100)}px, {random.randint(-100, 100)}px); }}
            100% {{ transform: translate(0, 0); }}
        }}
        """

    # HTML and CSS for the main page
    html_code = f"""
    <style>
        html, body {{
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }}
        body {{
            font-family: 'Arial', sans-serif;
            background-color: rgba(255, 255, 255, 0.5);
            background-size: cover;
            color: #202021;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background-color: transparent;
            position: relative;
        }}
        .header {{
            display: none;
        }}
        .direction-buttons {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem;
            width: 100%;
            padding: 0 2rem;
            position: relative;
            height: 600px;
            width: 600px;
        }}
        .direction-button {{
            padding: 1rem;
            width: 100px;
            height: 100px;
            background-color: rgba(84, 116, 111, 0.7);
            border-radius: 50%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: absolute;
            text-decoration: none;
            animation: move 60s infinite alternate ease-in-out;
        }}
        .direction-button img {{
            width: 50px;
            height: 50px;
            margin-bottom: 0.5rem;
            transition: transform 0.3s ease;
        }}
        .direction-button span {{
            color: #fff;
            font-weight: bold;
            flex: 1;
            text-align: center;
            font-size: 0.8rem;
        }}
        .direction-button:hover {{
            transform: scale(1.2);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            background-color: rgba(76, 104, 92, 0.9);
        }}
        .direction-button:hover img {{
            transform: scale(1.2);
        }}
        .tooltip {{
            visibility: hidden;
            width: 200px;
            background-color: rgba(0, 0, 0, 0.7);
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 10px;
            position: absolute;
            z-index: 1;
            bottom: 120%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        .tooltip::after {{
            content: '';
            position: absolute;
            top: 100%;
            left: 50%;
            margin-left: -5px;
            border-width: 5px;
            border-style: solid;
            border-color: rgba(0, 0, 0, 0.7) transparent transparent transparent;
        }}
        .direction-button:hover .tooltip {{
            visibility: visible;
            opacity: 1;
        }}
        {keyframes_styles}
    </style>
    """

    for index, (name, info) in enumerate(buttons.items()):
        random_x, random_y = positions[index]
        html_code += f"""
            <div onclick="window.parent.postMessage({{'page': '{info['page']}'}}, '*')" class="direction-button" style="left: {random_x}px; top: {random_y}px; animation: move{index} 60s infinite alternate ease-in-out;">
                <img src="data:image/png;base64,{encoded_images[name]}" alt="{name}"/>
                <span>{name}</span>
                <div class="tooltip">{info['tooltip']}</div>
            </div>
        """

    html_code += """
        </div>
    """

    # Embed HTML code
    components.html(html_code, height=800)

    # Add JavaScript to handle page navigation
    st.markdown("""
        <script>
        window.addEventListener('message', function(event) {
            if (event.data.page) {
                window.location.href = "/" + event.data.page;
            }
        });
        </script>
    """, unsafe_allow_html=True)


