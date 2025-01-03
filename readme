# Revan Artificial Intelligence System

Revan is an AI chatbot powered by Blenderbot, featuring SQLite integration to maintain chat history. It includes capabilities for memory management, offensive language filtering, and command-based operations.

## Features

- **AI-Powered Responses**: Uses the `BlenderbotForConditionalGeneration` model from Hugging Face.
- **Chat History Persistence**: Stores user inputs and chatbot responses in an SQLite database.
- **Internal Commands**:
  - `/internalcommand --wipe memory`: Clears all stored chat history.
  - `/internalcommand --recall history`: Retrieves and displays the chat history.
  - `/internalcommand --exit`: Exits the conversation.
- **Offensive Language Filtering**: Detects and blocks inappropriate language in user input.
- **Configurable Response Handling**: Ensures responses are not cut off or repeated unnecessarily.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sekyb/revan.git
    cd revan
    ```
    Go to https://huggingface.co/facebook/blenderbot-400M-distill to install this model and place it inside of revan.git

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the SQLite database:
    ```bash
    python
    >>> import sqlite3
    >>> conn = sqlite3.connect("chat_history.db")
    >>> cursor = conn.cursor()
    >>> cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        chatbot_response TEXT
    )
    """)
    >>> conn.commit()
    >>> conn.close()
    ```

4. Run the chatbot:
    ```bash
    python revan.py
    ```

## Usage

### Starting the Chatbot
Run the chatbot script using:
```bash
python revan.py
```

### Internal Commands
While interacting with the chatbot, use the following commands:

- `/internalcommand`: Display the internal command menu.
- `/internalcommand --wipe memory`: Clears all stored chat history.
- `/internalcommand --recall history`: Retrieves and displays the stored chat history.
- `/internalcommand --exit`: Exits the chatbot session.

### Offensive Language Filtering
The chatbot will not respond to inputs containing offensive words. Instead, it will return a default message:
> "I'm sorry, I cannot respond to offensive language."

## Code Overview

### Main Components

- **SQLite Database**: Stores user inputs and chatbot responses.
- **Blenderbot Model**: Handles the natural language processing tasks.
- **Conversation History**: Maintains in-session context.

### Key Functions

- `insert_chat_entry(user_input, chatbot_response)`: Saves chat data to the database.
- `get_chatbot_response(user_input)`: Processes user input and generates a response.
- `print_internal_command_menu()`: Displays available internal commands.
- `wipe_memory()`: Clears stored conversation data.
- `recall_chat_history()`: Displays stored chat history.
- `contains_offensive_language(text)`: Checks for offensive language in user input.
- `complete_response(response)`: Ensures chatbot responses are complete and not truncated.

## Requirements

- Python 3.8+
- SQLite
- Hugging Face Transformers library
- [Blenderbot 400M Distill](https://huggingface.co/facebook/blenderbot-400M-distill)

## Contributing

Feel free to fork the repository and submit pull requests. For significant changes, please open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Developed by [sekyb](https://github.com/sekyb)**
