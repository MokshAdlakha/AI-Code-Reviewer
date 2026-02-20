# 🚀 AI Code Reviewer

An AI-powered Code Review and Optimization Assistant that analyzes code snippets and provides complexity estimation, potential issue detection, and optimization suggestions using a hybrid approach combining static analysis and Large Language Models (LLMs).

---

## 📌 Features

✅ Time Complexity Estimation  
✅ Space Complexity Analysis  
✅ Edge Case Detection  
✅ Optimization Suggestions  
✅ Hybrid Static + AI Analysis  
✅ Secure API Key Handling using Environment Variables  
✅ Clean Web Interface  

---

## 🧠 How It Works

The system performs analysis in two stages:

1. **Static Analysis**
   - Detects loops (`for`, `while`)
   - Estimates algorithmic complexity.

2. **AI-Based Analysis**
   - Uses LLM API to understand logic.
   - Provides performance insights and improvements.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI Integration:** LLM API (Groq)
- **Environment Management:** python-dotenv
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

ai-code-reviewer/
│
├── services/
│ ├── ai_service.py
│ └── static_analysis.py
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
├── app.py
├── .gitignore
└── README.md

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-code-reviewer.git
cd ai-code-reviewer
2️⃣ Create Virtual Environment
python -m venv venv
Activate:

Windows

venv\Scripts\activate
3️⃣ Install Dependencies
pip install flask requests python-dotenv
4️⃣ Add Environment Variables
Create .env file:

API_KEY=your_api_key_here
5️⃣ Run Application
python app.py
Open browser:

http://127.0.0.1:5000
