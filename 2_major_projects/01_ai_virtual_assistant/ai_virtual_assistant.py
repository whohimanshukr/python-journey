"""
AI Virtual Assistant ("Space")
==============================
A multi-turn conversational AI assistant running on Groq Cloud LLM APIs.
Maintains conversational memory context and handles streaming responses.
"""

import os
import sys
from groq import Groq

# ---------------------------------------------------------
# 1. ENCODING CONFIGURATION (Cross-Platform / Windows UTF-8)
# ---------------------------------------------------------
# Ensures Windows terminal outputs special Unicode characters (e.g. emojis,
# non-breaking spaces, curly quotes) without raising 'charmap' codec errors.
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# ---------------------------------------------------------
# 2. SECURE API KEY SETUP (Environment Variable)
# ---------------------------------------------------------
# For security and best practices, never hardcode API keys in source code.
# The key is read directly from the 'GROQ_API_KEY' environment variable.
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    print("=" * 70)
    print("❌ ERROR: GROQ_API_KEY environment variable is not set!")
    print("=" * 70)
    print("\nTo obtain a free API key, register at: https://console.groq.com/keys\n")
    print("Set the key in your terminal before running this script:")
    print("  • Windows PowerShell:  $env:GROQ_API_KEY=\"your_api_key_here\"")
    print("  • Windows Command Prompt: set GROQ_API_KEY=your_api_key_here")
    print("  • Windows (Permanent): setx GROQ_API_KEY \"your_api_key_here\"")
    print("  • Linux / macOS:       export GROQ_API_KEY=\"your_api_key_here\"\n")
    print("=" * 70)
    sys.exit(1)


# ---------------------------------------------------------
# 3. GROQ CLIENT INITIALIZATION
# ---------------------------------------------------------
client = Groq(api_key=api_key)


# ---------------------------------------------------------
# 4. CONVERSATION MEMORY (STATE MANAGEMENT)
# ---------------------------------------------------------
# The messages list stores conversational history so the AI retains context
# across multiple question-and-answer turns.
# Structure: [{"role": "system" | "user" | "assistant", "content": "..."}]
messages = [
    {
        "role": "system",
        "content": (
            "You are Space, a helpful, polite, and intelligent AI personal assistant. "
            "You provide clear, accurate, and structured answers."
        ),
    }
]


# ---------------------------------------------------------
# 5. COMPLETION FUNCTION
# ---------------------------------------------------------
def completion(user_message: str) -> None:
    """
    Appends the user's message to conversation memory, requests a response
    from the Groq cloud model, records the assistant's reply, and displays it.
    """
    global messages

    # Step A: Append user's input to conversation history
    messages.append({
        "role": "user",
        "content": user_message,
    })

    try:
        # Step B: Request chat completion using an active Groq LLM model
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="openai/gpt-oss-120b",
        )

        # Step C: Extract the generated reply
        ai_reply = chat_completion.choices[0].message.content

        # Step D: Save assistant response into memory for follow-up questions
        messages.append({
            "role": "assistant",
            "content": ai_reply,
        })

        # Step E: Display reply
        print(f"\nSpace: {ai_reply}\n")

    except Exception as error:
        print(f"\n[Error communicating with Groq API]: {error}\n")


# ---------------------------------------------------------
# 6. INTERACTIVE CHAT LOOP
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=" * 65)
    print("🤖 Space: Hi! I am Space, your AI assistant. How may I help you today?")
    print("💡 (Type 'exit', 'quit', or 'bye' to end the conversation)")
    print("=" * 65 + "\n")

    while True:
        try:
            user_input = input("You: ").strip()

            # Ignore empty inputs
            if not user_input:
                continue

            # Check for exit commands
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\nSpace: Goodbye! Have a wonderful day! 👋\n")
                break

            # Send input to completion handler
            completion(user_input)

        except (KeyboardInterrupt, EOFError):
            print("\nSpace: Session closed. Goodbye! 👋\n")
            break
