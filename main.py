from PromptHandling.llm_query import get_LLM_response
from dotenv import load_dotenv
import openai
import os

def main():
    inputs = input("Enter the question you want to solve: ")
    print("You entered:", inputs)
    print("Now I will generate a response using the LLM.")

    additional_instructions = "Complete the following code: " #Might add some later, but system seems to do similar thing (in LLM_query)
    prompt = additional_instructions + inputs
    raw_output = get_LLM_response(prompt)
    raw_output = raw_output.replace("```", "").replace("def", "def ").replace("return", "return ").replace(":", ": ").replace("python", "")
    output = raw_output.strip().splitlines()

    split_index = find_split_index(output)
    print("Split index:", split_index)
    generated_code = "\n".join(output[:split_index])
    test_case = "\n".join(output[split_index:]) if split_index < len(output) else None

    print("Generated code:", generated_code)
    print("Test case:", test_case)

def find_split_index(lines):
    return next(
        (i for i, line in enumerate(lines) if line.strip() and not line.startswith(" ") and not line.startswith("def") and not line.startswith("```")),
        len(lines)
    )
if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()