

# Textbase: Building Chatbots with NLP and ML

[![Documentation](https://img.shields.io/website/http/huggingface.co/docs/transformers/index.svg?down_color=red&down_message=offline&up_message=online)](https://docs.textbase.ai)

Textbase is a powerful framework for building chatbots using natural language processing (NLP) and machine learning (ML) technologies. With Textbase, you can create chatbots that are both creative and intelligent, capable of engaging in meaningful conversations with users.

https://www.loom.com/share/4d7bfdc834e94b82a35b6b55569530ff?sid=195b79f6-5cba-4e13-9f23-46bfb795ad1c

## Getting Started

To use MindsDB in your Textbase chatbot, follow these steps:

### 1. Create a MindsDB Model

To integrate MindsDB into your chatbot, you'll need to create a MindsDB model. Use the following SQL query to create your model:

```sql
CREATE MODEL mindsdb.yenstein
PREDICT response
USING
engine = 'openai',
max_tokens = 300,
-- api_key = "not to reveal api key",
model_name = 'gpt-3.5-turbo',
temperature: 0.6,
prompt_template = 'From input message: {{text}}\
by from_user: {{author_username}}\
In less than 300 characters, write a Twitter response to {{author_username}} in the following format:\
@<from_user>,<respond like you are a fusion of Kanye West and Albert Einstein. Imagine you possess Kanyes unique style, confidence, and stream-of-consciousness speaking, combined with Einsteins intellect. Use inventive language and metaphors to express ideas with depth. Youre known for controversial insights and intellectual brilliance. Make references to Kanyes music and Einsteins scientific achievements.'
as my contributionn


This query defines a MindsDB model named "yenstein" that will predict the "response" based on the specified parameters.

### 2. Integration in `main.py`

Implement the `on_message` function in `main.py` of your Textbase chatbot. Textbase will handle the integration with MindsDB, allowing you to generate responses using the MindsDB model you created.

```python
# Implement the on_message function in main.py
# Textbase will handle the integration with MindsDB
# Your bot logic goes here
```

That's it! Textbase will take care of the rest, and your chatbot will be able to generate responses using the MindsDB model.

## Installation

Make sure you have Python version >= 3.9.0 installed. You can install Textbase using `pip` or by cloning the repository locally.

### Install via pip

```bash
pip install textbase-client
```

### Local Installation

Clone the repository and install the dependencies using Poetry:

```bash
git clone https://github.com/cofactoryai/textbase
cd textbase
poetry shell
poetry install
```

## Start Development Server

Before starting the development server, ensure you set your OpenAI API key in `main.py`.

Run the following command to start the development server:

- If installed locally:

  ```bash
  poetry run python textbase/textbase_cli.py test
  ```

- If installed via pip:

  ```bash
  textbase-client test
  ```

You will receive a link in the command line. Follow the link to chat with your bot, which now incorporates the MindsDB model for generating responses.

## Contributions

Contributions are welcome! Please open an issue or create a pull request to improve Textbase and its integration with MindsDB.
```

In this README update, we've added the steps to create a MindsDB model and integrate it into your Textbase chatbot, along with instructions on setting up and running your chatbot. Make sure to replace the placeholder values in the MindsDB model creation query with your actual configuration.
