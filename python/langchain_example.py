from typing import List
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field

use_openai = True

# Init model (OpenAI vs. OctoAI)
# Total changes: remove 3 LoCs, add 6 LoCs
if use_openai:
    # Use OpenAI LLM
    from langchain.llms import OpenAI
    # Make sure you've set OPENAI_API_KEY in your environment
    model = OpenAI(
        model_name="gpt-3.5-turbo"
    )
else:
    # Use OctoAI LLM
    from langchain.llms.octoai_endpoint import OctoAIEndpoint
    # Make sure you've set OCTOAI_API_TOKEN in your environment
    model = OctoAIEndpoint(
        endpoint_url="https://text.octoai.run/v1/chat/completions",
        model_kwargs={
            "model": "llama-2-70b-chat-fp16",
            "messages": [ {"role": "system", "content": "Below is an instruction that describes a task."} ],
        },
    )

prompt = PromptTemplate(
    template="Answer the user query.\n{query}\n",
    input_variables=["query"],
)

actor_query = "Generate the filmography for Tom Hanks."
_input = prompt.format_prompt(query=actor_query)
output = model(_input.to_string())

print(output)