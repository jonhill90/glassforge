import os
from openai import OpenAI
from server_mcp import build_prompt_context

def call_openai(prompt: str, model="gpt-4", temperature=0.7):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful development assistant working within a tool called Glassforge."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    prompt = build_prompt_context()
    print("📤 Sending prompt to OpenAI...\n")
    result = call_openai(prompt)
    print("📥 Response:\n")
    print(result)
