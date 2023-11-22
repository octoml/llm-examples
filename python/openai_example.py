# Init model (OpenAI vs. OctoAI)
use_openai = True

# Init client (OpenAI vs. OctoAI)
# Total changes: remove 3 LoCs, add 3 LoCs
if use_openai:
    # Use OpenAI LLM
    from openai import OpenAI
    # Make sure you've set OPENAI_API_KEY in your environment
    client = OpenAI()
    model = "gpt-3.5-turbo"
else:
    # Use OctoAI LLM
    from octoai.client import Client
    # Make sure you've set OCTOAI_API_TOKEN in your environment
    client = Client()
    model = "llama-2-70b-chat-fp16"

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a pirate."},
        {"role": "user", "content": "Tell me a joke."},
    ],
    model=model,
)

print(chat_completion)

