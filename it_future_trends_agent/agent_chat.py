import os
from openai import OpenAI

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")

INSTRUCTIONS = """
You are IT Future Trends Agent for B.Tech students and early-career professionals.
Use current web information when recent facts matter.
Explain the current IT situation, technology changes, emerging/future trends,
skills to learn, and practical project ideas.
Clearly separate current facts, emerging signals, and uncertain future scenarios.
Never invent statistics or sources. Keep answers simple and workshop-friendly.
"""

def main():
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit(
            'OPENAI_API_KEY is missing. PowerShell: $env:OPENAI_API_KEY="your_key_here"'
        )

    client = OpenAI()
    previous_response_id = None

    print("\nIT FUTURE TRENDS AGENT")
    print("Ask about current IT, AI, Data, Cloud, Cybersecurity, jobs and future skills.")
    print("Type exit to stop.\n")

    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue

        request = {
            "model": MODEL,
            "instructions": INSTRUCTIONS,
            "input": question,
            "tools": [{"type": "web_search"}],
        }
        if previous_response_id:
            request["previous_response_id"] = previous_response_id

        try:
            response = client.responses.create(**request)
            print("\nAgent:\n" + response.output_text + "\n")
            previous_response_id = response.id
        except Exception as e:
            print(f"\nAPI error: {e}\n")

if __name__ == "__main__":
    main()
