# 🤖 Sister Constance Chatbot
A terminal-based chatbot built using the OpenAI API, featuring a custom persona inspired by the Adepta Sororitas: Order of the Valorous Heart.

Sister Constance speaks with a disciplined and unwavering voice and addresses the user as a fellow soul under trial. 

## ⚔️ Features
- Custom persona-driven responses
- Terminal-based interaction loop
- Environment-based API key management
- Modular structure (main, client, persona)

## 🚀 Run
1) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2) Install dependencies:

```bash
pip install openai python-dotenv
```

3) Create a `.env` file, and add your OPENAI_API_KEY:

```env
OPENAI_API_KEY=your_api_key_here
```

4) Start the program:

```bash
cd src
python main.py
```

## 📑 Notes
- API key is required in `.env`
- No memory or logging yet

## 🧠 Future Improvements
- Refactor main loop 
- Add logging
- Add memory