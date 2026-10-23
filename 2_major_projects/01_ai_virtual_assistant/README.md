# 🤖 AI Virtual Assistant ("Space")

## 📚 What I Learned
This project demonstrates the implementation of a modern, multi-turn **Conversational AI Assistant** using cloud Large Language Model (LLM) APIs powered by Groq. It bridges fundamental programming with generative artificial intelligence.

### ✅ Concepts Covered
- **Cloud LLM API Integration**: Calling high-speed inference endpoints using the official `groq` Python SDK
- **Conversation Context & Memory**: Preserving multi-turn chat history (`system`, `user`, `assistant` message schemas)
- **Security Best Practices**: Loading API credentials securely via system environment variables (`os.environ`) without hardcoding secrets
- **Error Handling**: Graceful exception catching for network dropouts, rate limits, and API failures
- **Cross-Platform Console Compatibility**: Reconfiguring `sys.stdout` to UTF-8 on Windows to handle emojis, typography, and Unicode characters without `charmap` errors
- **Interactive CLI Loops**: Creating an interactive terminal session with break conditions and keyboard interrupt handling

---

## 🎯 Learning Objectives
1. Connect and authenticate with the Groq Cloud API
2. Structure message payloads following the OpenAI-standard chat completion format
3. Maintain conversational state across continuous turns
4. Keep secrets safe for open-source GitHub publication
5. Build a polite, responsive AI assistant persona in the terminal

---

## 🔑 API Key Setup

This project requires a free Groq API key:

1. Create a free account at [Groq Cloud Console](https://console.groq.com/).
2. Generate an API key from the **API Keys** section.
3. Set the key in your terminal environment before running:

### Windows PowerShell:
```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
```

### Windows Command Prompt (CMD):
```cmd
set GROQ_API_KEY=your_groq_api_key_here
```

### Windows (Permanent for your user account):
```cmd
setx GROQ_API_KEY "your_groq_api_key_here"
```

### Linux / macOS:
```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

---

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the assistant**:
   ```bash
   python ai_virtual_assistant.py
   ```

---

## 📝 Example Output

```text
=================================================================
🤖 Space: Hi! I am Space, your AI assistant. How may I help you today?
💡 (Type 'exit', 'quit', or 'bye' to end the conversation)
=================================================================

You: What is the speed of light?
Space: The speed of light in a vacuum is approximately 299,792,458 meters per second (about 300,000 km/s or 186,282 miles per second).

You: How long does it take for light from the Sun to reach Earth?
Space: It takes approximately 8 minutes and 20 seconds for sunlight to reach Earth, traveling across an average distance of about 149.6 million kilometers (93 million miles).

You: quit
Space: Goodbye! Have a wonderful day! 👋
```

---

## 🔧 Features
- **Context Retention**: Remembers previous questions and answers in the same session
- **High-Speed Inference**: Powered by Groq's low-latency LPU inference engine
- **Safe Credential Handling**: Zero hardcoded keys; safe for version control
- **Graceful Termination**: Handles `exit`, `quit`, `bye`, and `Ctrl + C` cleanly
- **Custom AI Persona**: Pre-configured system instructions as "Space", an intelligent, courteous assistant

---

## 📈 Learning Progression
This project builds upon:
- ✅ Functions and modularity
- ✅ Lists and dictionaries (message payload history)
- ✅ Exception handling (`try-except`)
- ✅ System and OS modules (`os.environ`, `sys.stdout`)

Next steps will include:
- 🔄 Adding voice input/output (Speech-to-Text & Text-to-Speech)
- 📊 Streaming token responses in real-time
- 🌐 Adding a graphical interface (Tkinter / PyQt / Streamlit)
- 📁 Local conversation logging (saving chats to Markdown / JSON)

---

## 🎓 Real-World Application
Conversational AI assistants power:
- Customer service bots and virtual support agents
- Personal productivity and coding assistants
- Interactive education and tutoring tools
- In-car and IoT smart home voice interfaces

---
*Major Project #01 in my Python learning journey* 🐍
