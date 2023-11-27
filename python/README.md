## Getting started

### Watch the video on how easy it is to transition from OpenAI GPT-3.5 to Llama70B on OctoAI

[Video Link](https://www.loom.com/share/8e17cdb631364df988750bd957533fc0?sid=bd06546f-3f30-4e93-afd5-e6f566403058)

### Create a Python virtual environment

```python
python3 -m venv .venv
source .venv/bin/activate
```

### Install the python requirements

```python
python3 -m pip install -r requirements.txt
```

### Obtain an OpenAI API key

Refer to the following link: https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key

Make sure to add it to your environment with

```bash
export OPENAI_API_KEY="..."
```

### Obtain an OctoAI API token

Refer to the following link: https://docs.octoai.cloud/docs/how-to-create-an-octoai-access-token

Make sure to add it to your environment with

```bash
export OCTOAI_API_TOKEN="..."
```

### Run the examples

By default you'll be using OpenAI GPT3.5-turbo:

```bash
python3 openai_example.py
python3 langchain_example.py
```

To change to OctoAI's Llama2-70b, change the following line from:

```python
use_openai = True
```

to:

```python
use_openai = False
```

### LLM Options

There are several open source LLMs at your disposal that you can test out, with different quality and performance tradeoffs depending on the use case:

* `codellama-13b-instruct-fp16`
* `codellama-34b-instruct-int4`
* `codellama-34b-instruct-fp16`
* `codellama-7b-instruct-fp16`
* `llama-2-13b-chat-fp16`
* `llama-2-70b-chat-fp16`
* `llama-2-70b-chat-int4`
* `mistral-7b-instruct-fp16`
