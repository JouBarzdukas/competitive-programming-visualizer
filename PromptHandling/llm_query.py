import openai

def get_coding_LLM_response(prompt) -> str:
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions="You're an expert competitive programmer. Write a concise Python function that solves the problem below. Only include code (no comments or explanation). After the function, provide one valid test case using the same variable names as in the function. Example format: 's = [1, 2, 3], k = 2'.",
        input=prompt,
    )
    return response.output_text

def get_step_by_step_instructions(prompt, test_case) -> str:
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions="Suppose you are an animator's assistant which specialises in education. You are tasked with writing code which shows exactly what is going on given a method and some test variables. The animator needs you to give step by step instructions on what digital movements should be going on to best make this animation work. By that, I mean you should state EXACTLY what should be happening at each step and telling me HOW it should be animated. Start each step with ""Step X:"" where X is the step number. Utilize the given test case",
        input= prompt + "\n" + test_case,
    )
    return response.output_text
def get_manim_animation_output(prompt) -> str:
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions="Write the manim code for the following problem. To ensure proper animation style, all boxes should be properly spaced from each other and all labels should also be properly spaced. Utilize no SVG, and ensure that there is always an arrow pointing at where you current are in the code. Write all code out in full. Things should be BOXED and ANIMATED. Do not include any explanation. Be aware of things overlapping and put things in the right place.",
        input=prompt,
    )
    return response.output_text