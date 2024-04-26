
# Pybot Chatbot

Welcome to Pybot Chatbot! Pybot is a simple chatbot developed using Python and deployed on Azure App Service with Flask. It's designed to respond to user queries about Python, modules, and general greetings.

## Features

- **Greeting:** Pybot can greet users with various responses when they say hello or hi.
- **Python Query:** It provides information about Python programming language when asked.
- **Module Query:** Pybot can explain what a module is in Python.
- **Introductions:** Pybot introduces itself when asked about its name.

## How It Works

Pybot uses various natural language processing (NLP) techniques to understand and respond to user queries:

### Tokenization

Tokenization is the process of breaking text into words or phrases, known as tokens. Pybot uses the `nltk.word_tokenize()` function from the Natural Language Toolkit (NLTK) to tokenize input sentences into words.

### Stemming

Stemming is the process of reducing words to their root form by removing suffixes. However, Pybot does not perform stemming in this project.

### Lemmatization

Lemmatization is similar to stemming, but it reduces words to their base or dictionary form (lemma). Pybot uses the WordNet lemmatizer from NLTK (`nltk.stem.WordNetLemmatizer()`) to lemmatize tokens. This helps in standardizing words and improving response accuracy.

## Deployment

The Pybot chatbot is deployed on Azure App Service using Flask. Flask allows Pybot to handle HTTP requests and responses, enabling it to interact with users over the web. You can access Pybot through the following link: [Pybot Chatbot](https://python-pybot.azurewebsites.net/)

## Usage

1. **Greeting:** Say hello or hi to start a conversation with Pybot.
2. **Python Query:** Ask Pybot about Python by typing questions like "What is Python?" or "Tell me about Python."
3. **Module Query:** Inquire about modules in Python by asking questions such as "What is a module?" or "Explain Python modules."
4. **Introductions:** Ask Pybot about its name or introduction to learn more about it.

## Future Improvements

- Incorporate more advanced NLP techniques for better understanding and responses.
- Expand Pybot's knowledge base to cover a wider range of topics.
- Enhance the user interface for a more interactive experience.

