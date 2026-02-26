
# 🤖 QBot – Generative AI FAQ Chatbot

A simple AI-powered chatbot built using **Generative AI API** and **Streamlit** that answers user queries in a conversational format.



## 📌 About The Project

QBot is a conversational AI chatbot developed as part of a **Generative AI course project**.

Instead of training a machine learning model from scratch, this chatbot integrates a **pre-trained Large Language Model (LLM)** through API to generate intelligent responses in real-time.

The chatbot demonstrates how modern Generative AI systems can be used to build interactive FAQ assistants.



## How It Works

1. User enters a question in the Streamlit interface.
2. The input is sent to the Generative AI model via API.
3. The model processes the text and generates a response.
4. The response is displayed in the chat interface.

###  Architecture Flow

User → Streamlit UI → API Call → LLM (Gemini) → Response → UI Display



##  Features

* Conversational AI interface
* Real-time response generation
* Session-based chat memory
* Error handling
* Clean and interactive UI



##  Tech Stack

* **Python**
* **Streamlit**
* **Gemini API (Generative AI)**
* **dotenv (API key management)**



##  Project Structure

```
QBot/
│── app.py
│── requirements.txt
│── README.md
│── .env (not uploaded)
```



##  Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/QBot.git
cd QBot
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Add your API Key

Create a `.env` file and add:

```
API_KEY=your_api_key_here
```

### 4️⃣ Run the app

```
streamlit run app.py
```

---

## 🎯 Why No Model Training?

This project is built using a **pre-trained Large Language Model** via API.

Therefore:

* No dataset splitting required
* No manual preprocessing required
* No training or evaluation metrics required

All NLP processing is handled internally by the LLM.



##  Learning Outcomes

* Understanding Generative AI concepts
* API-based LLM integration
* Prompt-based response generation
* Building UI using Streamlit
* Deploying AI applications

---

## 📌 Future Improvements

* Domain-restricted FAQ control
* Knowledge-base integration
* Deployment on cloud
* Adding authentication system


