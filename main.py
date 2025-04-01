from PromptHandling.llm_query import get_LLM_response
from dotenv import load_dotenv
import openai
import os

def main():
    prompt = "Could you write a one paragraph summary of 1984, and a one paragraph summary of the hunger games'?"
    output = get_LLM_response(prompt)
    print(output)

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()