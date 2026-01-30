import streamlit as st
import base64

st.set_page_config(layout="wide")

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Bannière ---
st.markdown(
    """
    <div style="
        background-color:#f4d03f;
        padding:20px;
        border-radius:10px;
        text-align:center;
        margin-bottom:20px;
    ">
        <h1 style="color:#ffffff; margin:0; font-size:32px;">
            🚑 Outil de suivi boursier – Fnac Darty
        </h1>
        <p style="color:#004fa3; font-size:18px; margin:0;">
            Analyse consolidée sur une période déterminée
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

bg_image = get_base64_image("assets/KPIs_FNC_DTY.png")

st.markdown(
    f"""
    <style>
    .image-container {{
        position: relative;
        max-width: 900px;
        margin: 5vh auto;
    }}

    .image-container img {{
        width: 100%;
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    }}

    .text-overlay {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(0, 0, 0, 0.65);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        width: 80%;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="image-container">
        <img src="data:image/png;base64,{bg_image}">
    </div>
    """,
    unsafe_allow_html=True
)
