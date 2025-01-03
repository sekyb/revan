import sqlite3
from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

# Connect to the SQLite database
conn = sqlite3.connect("chat_history.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS chat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        chatbot_response TEXT
    )
    """
)
conn.commit()

# Load the Blenderbot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Maintain conversation history
conversation_history = []

# Define a function to insert a chat entry into the database
def insert_chat_entry(user_input, chatbot_response):
    cursor.execute(
        """
        INSERT INTO chat (user_input, chatbot_response)
        VALUES (?, ?)
        """,
        (user_input, chatbot_response),
    )
    conn.commit()

# Define a function to process user input and generate a response
def get_chatbot_response(user_input):
    global conversation_history
    chatbot_response = ""

    # Check for offensive language
    if not contains_offensive_language(user_input):
        # Generate a response from the model
        chatbot_response_ids = model.generate(
            tokenizer.encode(user_input, return_tensors="pt"),
            max_length=1000,
            num_return_sequences=1,
            no_repeat_ngram_size=3,
            do_sample=True,
            temperature=0.7,
        )
        chatbot_response = tokenizer.decode(chatbot_response_ids[0], skip_special_tokens=True)

    # Save the chat entry in the database if it's not offensive and not a repetition
    if not contains_offensive_language(user_input) and (not conversation_history or chatbot_response != conversation_history[-1]):
        conversation_history.append(chatbot_response)

    # Ensure the response is not cut off
    chatbot_response = complete_response(chatbot_response)

    # If chatbot_response is empty (offensive language), provide a default response
    if not chatbot_response:
        chatbot_response = "I'm sorry, I cannot respond to offensive language."

    return chatbot_response

# Define a function to check for offensive language
def contains_offensive_language(text):
    offensive_words = ["fuck", "asshole", "bitch", "shit", "damn", "bastard", "idiot", "stupid", "moron"]  # Comprehensive list of offensive words
    for word in offensive_words:
        if word in text.lower().split():
            return True
    return False

# Define a function to ensure the response is complete
def complete_response(response):
    if len(response) > 1000:
        response = response[:1000] + " [Response truncated]"
    return response

# Command line interaction
print("*** Welcome to Haruko Chatbot ***")
print("Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Haruko: Goodbye!")
        break

    # Error handling for empty user input
    if not user_input.strip():
        print("Haruko: Please enter something.")
        continue

    chatbot_response = get_chatbot_response(user_input)
    print("Haruko:", chatbot_response)

# Close the SQLite connection
conn.close()
