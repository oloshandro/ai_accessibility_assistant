# 🧠 AI Accessibility Assistant – Chernihiv

An AI-powered assistant that helps users find accessible public places in the city of Chernihiv. It uses up-to-date real data and conversational AI to answer questions about accessibility infrastructure like ramps, braille signs, and more.

---

## 🚀 Features

- Conversational AI assistant to answer questions about accessibility
- Real data from Chernihiv city (CSV-based)
- Fast, lightweight, and customizable backend (Flask-based)
- HTML interface for basic interaction

---
## 🗂️ Project Structure

```text
AI_ACCESSIBILITY_ASSISTANT/
│
├── app/
│   ├── knowledge/                    # Accessibility data and vectorstore
│   │   ├── accessibility_chernihiv.csv
│   │   ├── accessibility_data_with_text.csv
│   │   └── vectorstore/             # Vector index files (optional)
│   │
│   ├── models/                      # Main AI assistant logic
│   │   ├── chat.py                  # Loads and queries the LLM
│   │   ├── prompt_helpers.py        # Prompt formatting utilities
│   │   ├── utils.py                 # Support functions
│   │   └── test.ipynb               # Testing notebook
│   │
│   ├── templates/
│   │   └── index.html               # Basic web interface
│   └── __init__.py
│
├── config.py                        # Configuration variables
├── run.py                           # App entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # 📘 You are here
└── .env                             # API keys and secrets (not included)
```

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

`git clone https://github.com/your-username/ai-accessibility-assistant.git
cd ai-accessibility-assistant`


2. **Install dependencies:**

`pip install -r requirements.txt`

3. **Add environment variables:**

Create a `.env` file with your API keys and model parameters:

OPENAI_API_KEY=your-api-key
GOOGLE_API_KEY=your-api-key

4. **Run the app:**

`python run.py`


## 💡 How It Works

- Loads data from a CSV file (`accessibility_data_with_text.csv`)
- Converts accessibility fields into structured text format
- Uses an LLM (Gemini, OpenAI or local) to answer questions about the data in Ukrainian
- Presents the result through a web interface or API call

---

## ✅ Data Fields (Sample)

Each place has fields like:

- **Назва** (Name)  
- **Адреса** (Address)  
- **Тип закладу** (Type)  
- **Пандус** (Ramp)  
- **Табличка з шрифтом Брайля** (Braille signage)  
- **Кнопка виклику персоналу** (Call button)  
- **Широкі двері** (Wide doors)

---

## 📌 Future Steps

- Expand dataset and update LLM knowledge base  
- Build a locally hosted LLM trained for the Ukrainian language
- Add voice mode for accessibility and ease of use
- Multilingual support (Ukrainian / English)
- Improve UI/UX for public use
- Integrate with social media bot system
- Expand coverage to other Ukrainian cities  

---
