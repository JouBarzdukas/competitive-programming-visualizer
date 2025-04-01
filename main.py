from PromptHandling.llm_query import get_coding_LLM_response
from PromptHandling.llm_query import get_step_by_step_instructions
from PromptHandling.llm_query import get_manim_animation_output
from PromptHandling.prompt_parsing import parse_output
from PromptHandling.prompt_parsing import get_video_code
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

    # For now, just get send raw_output to LLM for manim code
    manim_code = get_manim_animation_output(raw_output)
    generated_code = get_video_code(manim_code)

    print(generated_code)

    

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()