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

## Workflow Nodes Breakdown 🔄
 
**PPT Generation using N8N and Streamlit**

| Node                  | Purpose                                   | Key Details                                                   |
|-----------------------|-------------------------------------------|---------------------------------------------------------------|
| Webhook               | Receives prompt from Streamlit app        | Method: POST, handles prompt in request body                  |
| AI Agent              | Generates Python code for creating PPT    | Uses a system prompt defining formatting rules and slide structure |
| Google Gemini Chat Model | AI backend for the agent               | Connected as the LLM powering responses                       |
| Respond to Webhook    | Sends generated code back to Streamlit    | Returns AI-generated PPT script to user                       |

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

**1️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**2️⃣ Run the Streamlit app**
```bash
streamlit run app.py
```

---

## 🔗 API Integration
**Update the webhook URL inside app.py if needed:**
```python
requests.post(
    url="https://<your-n8n-instance>/webhook/<webhook-id>",
    json={"prompt": prompt}
)
```
---

## 📹 Demo Video
**👉 Watch the full workflow demo here:**
### [*AI PowerPoint Generator Automation*](https://www.linkedin.com/posts/challa-rakesh-reddy_ai-automation-generativeai-activity-7401875127677939713-EXUW?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD7NTjAB5LIcCGe6w75x6giyS2sV95rQD14)

---
<img width="1919" height="1051" alt="Screenshot 2025-12-03 115614" src="https://github.com/user-attachments/assets/cb9d34a4-b3d9-41ca-9e68-76432c30661e" />
