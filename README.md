# 📊 AI PowerPoint Generator (Streamlit + n8n + Gemini)

This project automates the creation of PowerPoint presentations using AI!  
Users submit their content through a stylish Streamlit app, which communicates with an n8n workflow integrated with Google Gemini to generate a `.pptx` file dynamically.

---

## 🚀 Features

✔ AI-Powered slide content generation  
✔ Automated PowerPoint creation  
✔ Beautiful and user-friendly Streamlit UI  
✔ Quick download after generation  
✔ Secure backend automation via n8n  

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend Automation | n8n Workflow |
| AI Content Generation | Google Gemini (via LangChain in n8n) |
| Presentation Engine | python-pptx |
| Communication | REST Webhook |

---

## 🧩 Project Architecture

Streamlit App → Sends user prompt → n8n Webhook  
→ Gemini AI generates python code → Returned to Streamlit  
→ Code executed locally → `.pptx` generated → User downloads

---

## 📌 How It Works

1️⃣ User describes PPT topic and structure  
2️⃣ Streamlit sends prompt to n8n webhook  
3️⃣ AI Agent generates Python code for slide creation  
4️⃣ Code is executed using python-pptx  
5️⃣ Output presentation made available to download  

---

## 🔧 Installation & Setup

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit app
```bash
pip install -r requirements.txt
```

---

## 🔗 API Integration
### Update the webhook URL inside app.py if needed:
```python
requests.post(
    url="https://<your-n8n-instance>/webhook/<webhook-id>",
    json={"prompt": prompt}
)
```
