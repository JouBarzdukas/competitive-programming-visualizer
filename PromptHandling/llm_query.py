import openai

def get_coding_LLM_response(prompt) -> str:
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions="You're an expert competitive programmer. Write a concise Python function that solves the problem below. Only include code (no comments or explanation). After the function, provide one valid test case using the same variable names as in the function. Example format: 's = [1, 2, 3], k = 2'.",
        input=prompt,
    )
    return response.output_text

def get_step_by_step_instructions(prompt, test_case) -> str:
    instruction = (
        "You're an educational animation planner. Given a Python function and a test case, "
        "describe what the animation should show at each step of execution. Use clear steps like: "
        "'Step 1: Show the input array at the top center. Step 2: Highlight index 0 with a yellow box.' "
        "Use concrete animations such as 'highlight', 'move arrow', 'show variable update', 'fade in/out'. "
        "Each step should begin with 'Step X:' and be clearly visualizable by a programmer with Manim experience. "
        "Avoid long descriptions—stick to simple, clear, frame-by-frame visuals."
    )
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions = instruction,
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