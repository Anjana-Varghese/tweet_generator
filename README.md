## Tweet Generator

Generate creative, informative, or witty tweets in one click — powered by **Google Gemini AI** and built with **Streamlit**.

---

## ✨ Features

- 📝 Choose a **tweet topic**
- 🎭 Select a **tone** (Formal, Informal, Witty, etc.)
- 🎯 Target a **specific audience**
- 🔖 Add **hashtags**
- 🧠 Powered by Google's **Gemini 1.5** via `google-generativeai`
- ⚡ Built with **Streamlit** for an easy-to-use web interface

---

## 🚀 Live App

👉 [Launch App on Streamlit](https://tweetgenerator123.streamlit.app/)  


---

📓 Original Colab Notebook
This project was first created in Google Colab using ipywidgets for the UI and Gemini's API for content generation.

📄 [View Original Notebook](https://github.com/Anjana-Varghese/tweet_generator/blob/main/colab-version/tweet_gen.ipynb)


## 🔧 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/Anjana-Varghese/tweet-generator.git
cd tweet-generator

2. Set up virtual environment (optional)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add .env file (local only)
Create a .env file in the root folder:
Token=your-api-key-here
🔐 Never share your .env file — it’s listed in .gitignore


5. Run the app
streamlit run app.py

