
# 🤖 AI Support Chatbot (Flask Project)

An AI-powered web application designed to process and respond to user queries through a modern chatbot interface.  
Built using **Flask** for backend API handling and **HTML/CSS/JavaScript** for a responsive frontend, the system leverages **NLP techniques** to interpret user inputs and generate context-aware responses.  
The project includes a **professional home page** and an **interactive chatbot UI** for real-time communication with the AI engine.


##  Features

-  AI-powered chatbot response system
-  Professional Home Page UI
-  Modern Chatbot Interface
-  Fast responses via Flask API
-  Clean & responsive UI with custom CSS
-  Smooth navigation between Home & Chatbot pages


##  Tech Stack

**Frontend**
- HTML5
- CSS3
- JavaScript (Fetch API)

**Backend**
- Python
- Flask


## 📁 Project Structure


AI_Project/
│
├── backend/
│   ├── app.py
│   ├── model/
│   │   └── chatbot_logic.py
│
├── templates/
│   ├── index.html
│   └── chatbot.html
│
├── static/
│   └── style.css
│
├── venv/
└── README.md


##  Setup Instructions

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
````

### 2️⃣ Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

---

## ▶️ Run the Application

```bash
cd backend
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000/
```

---

## Application Routes

| URL        | Description         |
| ---------- | ------------------- |
| `/`        | Home Page           |
| `/chatbot` | Chatbot UI          |
| `/chat`    | API endpoint (POST) |



## How Chat Works

1. User types a message
2. Message is sent to `/chat` via Fetch API
3. Flask processes input using `chatbot_logic.py`
4. AI response is returned as JSON
5. Message is displayed in the chat UI


## UI Highlights

* Gradient blue buttons (consistent theme across pages)
* Rounded chat bubbles
* Fixed input bar with aligned Send button
* Scrollable chat area
* Online status indicator


## Internship-Ready Points

* Clear MVC-like project structure
* API-based communication between frontend & backend
* Clean UI/UX for professional presentation
* Easily extendable to include:

  * Advanced NLP models
  * HuggingFace Transformers
  * Database logging
  * User authentication

##  Future Improvements

* Integrate Transformer/BERT models for smarter responses
* Store and retrieve chat history
* Implement user login system
* Enable voice input/output
* Add Dark Mode UI


<img width="1313" height="598" alt="image" src="https://github.com/user-attachments/assets/e9695b9d-779c-46c5-98d6-ea6d4d1a79aa" />

<img width="497" height="604" alt="image" src="https://github.com/user-attachments/assets/8a8b35e9-7b04-4a3c-be92-ce1ff95381b9" />



