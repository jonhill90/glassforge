import os
import openai
from server_mcp import build_prompt_context

def call_openai(prompt: str, model="gpt-4", temperature=0.7):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful development assistant working within a tool called Glassforge."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
    )

    return response.choices[0].message["content"].strip()


if __name__ == "__main__":
    prompt = build_prompt_context()
    print("📤 Sending prompt to OpenAI...\n")
    result = call_openai(prompt)
    print("📥 Response:\n")
    print(result)
