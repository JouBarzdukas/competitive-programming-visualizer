from PromptHandling.llm_query import get_coding_LLM_response
from PromptHandling.llm_query import get_step_by_step_instructions
from PromptHandling.prompt_parsing import parse_output
from dotenv import load_dotenv
import openai
import os

def main():
    inputs = input("Enter the question you want to solve: ")
    print("You entered:", inputs)
    print("Now I will generate a response using the LLM.")

    additional_instructions = "Complete the following code: " #Might add some later, but system seems to do similar thing (in LLM_query)
    prompt = additional_instructions + inputs

    # Ask how to do coding problem
    raw_output = get_coding_LLM_response(prompt)
    generated_code, test_case = parse_output(raw_output)

    # Get step by step instructions for coding problem
    raw_output = get_step_by_step_instructions(generated_code)

    

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()