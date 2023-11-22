## Getting started

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