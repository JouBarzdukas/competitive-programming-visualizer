from PromptHandling.llm_query import get_coding_LLM_response
from PromptHandling.llm_query import get_step_by_step_instructions
from PromptHandling.llm_query import get_animation_DSL
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

    additional_instructions = "Complete the following code: " #Might add some later, but system is doing similar thing (in LLM_query)
    prompt = additional_instructions + inputs

    print("Solving Question")
    # Ask how to do coding problem
    raw_output = get_coding_LLM_response(prompt)
    generated_code, test_case = parse_output(raw_output)

    print("Solving Question | FINISHED")
    print("Getting step by step instructions")
    # Get step by step instructions for coding problem
    raw_output = get_step_by_step_instructions(generated_code, test_case)

    print("Step by Step Instructions | FINISHED")
    print("Generating Animation DSL")
    # Get animation DSL from step by step instructions
    animation_DSL = get_animation_DSL(raw_output)

    print("Animation DSL | FINISHED")
    print("Generating Manim Code")
    manim_code = get_manim_animation_output(animation_DSL)
    generated_code = get_video_code(manim_code)


    # Save the generated code to a temporary file
    with open("generated_manim_script.py", "w") as f:
        f.write(generated_code)

    # Run the manim script using os.system or subprocess
    os.system("manim generated_manim_script.py")  # Ensure 'manim' is in your PATH


    

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()