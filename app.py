# import streamlit as st
# import requests
# import subprocess
# import sys
# st.title("AGENTIC BASED POWER POINT GENERATOR")

# prompt = st.text_area("please write the details of how you want to create the ppt")

# if st.button("generate ppt"):
#     if prompt:
#         response = requests.post(url="https://raghu1010.app.n8n.cloud/webhook/8f21a89c-4878-41b3-8f3a-15c4f3045f1b",
#                                  json={"prompt":prompt})
        
#         if response.status_code==200:
#             st.write("success")

#             with open("app1.py","w") as file:
#                 # response.json()["output"].strip("```python")  #+"\n prs.save('file.pptx')"
#                 file.write(response.json()["output"].strip("```python"))

#             subprocess.run([sys.executable,"app1.py"])


# with open(r"C:\Users\rake0\Downloads\Agentic AI\power\Agentic_AI_Presentation.pptx", "rb") as f1:
#         st.download_button(
#             label="Download pptx",
#             data=f1,
#             file_name="data.pptx")


import streamlit as st
import requests
import subprocess
import sys
import time

# Page configuration
st.set_page_config(
    page_title="AI PowerPoint Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for advanced styling
st.markdown("""
    <style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Custom container styling */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        margin: 2rem auto;
        max-width: 1200px;
    }
    
    /* Title styling */
    .custom-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: #000;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Subtitle styling */
    .custom-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Text area styling */
    .stTextArea>div>div>textarea {
        border-radius: 15px;
        border: 2px solid #e0e0e0;
        padding: 1rem;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextArea>div>div>textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Success message */
    .success-message {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: 600;
        margin: 1rem 0;
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Download button custom styling */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        font-weight: 600;
        border-radius: 50px;
        padding: 0.75rem 2rem;
        border: none;
        width: 100%;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(17, 153, 142, 0.4);
    }
    
    .stDownloadButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(17, 153, 142, 0.6);
    }
    
    /* Info boxes */
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* Progress bar custom */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 📊 About")
    st.markdown("""
    This AI-powered tool generates professional PowerPoint presentations 
    based on your requirements.
    """)
    
    st.markdown("### ✨ Features")
    st.markdown("""
    - 🤖 AI-Powered Generation
    - 🎨 Professional Designs
    - ⚡ Fast Processing
    - 📥 Instant Download
    """)
    
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. Enter your presentation details
    2. Click 'Generate Presentation'
    3. Wait for processing
    4. Download your PPT
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Be specific about topics
    - Mention slide count
    - Specify design preferences
    - Include key points
    """)

# Main content
st.markdown('<h1 class="custom-title">📊 AI PowerPoint Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="custom-subtitle">Transform your ideas into stunning presentations with AI</p>', unsafe_allow_html=True)

# Feature highlights
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <h3 style="text-align: center;">🚀 Fast</h3>
            <p style="text-align: center;">Generate presentations in seconds</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <h3 style="text-align: center;">🎨 Beautiful</h3>
            <p style="text-align: center;">Professional designs automatically</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <h3 style="text-align: center;">🤖 Smart</h3>
            <p style="text-align: center;">AI-powered content generation</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main input section
with st.container():
    st.markdown("### 📝 Describe Your Presentation")
    st.markdown('<div class="info-box">💡 Tip: Include topic, number of slides, key points, and design preferences</div>', unsafe_allow_html=True)
    
    # YOUR ORIGINAL CODE STARTS HERE (UNMODIFIED)
    prompt = st.text_area("please write the details of how you want to create the ppt", height=200, placeholder="Example: Create a 10-slide presentation about Climate Change with sections on causes, effects, and solutions. Use a professional blue theme.")

    if st.button("🎯 Generate Presentation"):
        if prompt:
            with st.spinner('🔮 AI is crafting your presentation...'):
                progress_bar = st.progress(0)
                
                # Simulate progress
                for i in range(30):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                response = requests.post(url="https://raghu1010.app.n8n.cloud/webhook/8f21a89c-4878-41b3-8f3a-15c4f3045f1b",
                                        json={"prompt":prompt})
                
                progress_bar.progress(60)
                
                if response.status_code==200:
                    st.markdown('<div class="success-message">✅ Presentation Generated Successfully!</div>', unsafe_allow_html=True)

                    with open("app1.py","w") as file:
                        file.write(response.json()["output"].strip("```python"))
                    
                    progress_bar.progress(80)
                    
                    subprocess.run([sys.executable,"app1.py"])
                    
                    progress_bar.progress(100)
                    time.sleep(0.5)
                    progress_bar.empty()
                    
                    st.balloons()
                else:
                    st.error("❌ Failed to generate presentation. Please try again.")
        else:
            st.warning("⚠️ Please enter presentation details before generating.")

    # YOUR ORIGINAL CODE ENDS HERE

st.markdown("<br>", unsafe_allow_html=True)

# Download section with enhanced styling
st.markdown("### 📥 Download Your Presentation")

try:
    with open(r"C:\Users\rake0\Downloads\Agentic AI\power\Agentic_AI_Presentation.pptx", "rb") as f1:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="⬇️ Download PowerPoint",
                data=f1,
                file_name="AI_Generated_Presentation.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
except FileNotFoundError:
    st.info("📌 Your presentation will appear here after generation")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: white; padding: 2rem;">
        <p style="font-size: 0.9rem;">Made with ❤️ using Streamlit & AI</p>
        <p style="font-size: 0.8rem;">© 2024 AI PowerPoint Generator. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)