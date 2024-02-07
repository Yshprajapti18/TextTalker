# TextTalker: AI Chatbot with Django Backend

TextTalker is an AI-powered chatbot built with Django that offers seamless communication between users and the AI model. The chatbot integrates with the HuggingChat API for enhanced chat functionality and includes user authentication and chat storage features.

![Screenshot 2023-11-11 012634](https://github.com/Yshprajapti18/Django-Chatbot/assets/128960060/be160180-3241-4ca6-91c9-24961e3575d6)


## Features

- **User Authentication**: Secure user registration and login system to manage user access.

- **Chat Storage**: Store and retrieve chat history for users.

- **HuggingChat API Integration**: Seamlessly integrate with the HugChat API for AI chatbot capabilities.

- **Interactive UI**: Enhance the user experience with a responsive and interactive user interface powered by JavaScript.

## Getting Started

These instructions will help you get your project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django
- HugggingChat account (get it [here](https://huggingface.co/chat/))

### Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/Yshprajapti18/Django-Chatbot.git
  cd texttalker
  ```
2.Create a virtual environment and install dependencies:

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  pip install -r requirements.txt
  ```
3.Set up the database and apply migrations:

  ```bash
  python manage.py migrate
  ```
4.Configure API keys:

  Obtain your HuggingChat account and password and add it to your Django settings or make a .env file with 'EMAIL' and 'PASSWORD'.

6.Start the development server:

  ```bash
  python manage.py runserver
  ```
### Usage

   - Register and log in to start chatting with the AI assistant.

   - Interact with the chatbot by sending messages and receiving responses.

   - Review and access chat history in your user profile.

### Contrubuting

   1. Fork the repository.

   2. Create a new branch for your feature or bug fix.

   3. Make your changes and write tests if applicable.

   4. Ensure your code follows the project's coding style.

   5. Submit a pull request.

### Acknowledgement

Special thanks to the developers and contributors of Django, HugChat, and other open-source libraries used in this project.
