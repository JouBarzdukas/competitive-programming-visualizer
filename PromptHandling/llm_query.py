import openai

def get_coding_LLM_response(prompt) -> str:
    instruction = (
        "You're an expert competitive programmer. "
        " Write a concise Python function that solves the problem below. "
        "Only include code (no comments or explanation). "
        "After the function, provide one valid test case using the "
        "same variable names as in the function. "
        "Example format: 's = [1, 2, 3], k = 2'."
    )
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions=instruction,
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
    instruction = (
        "You're a Manim animator. Given a step-by-step animation plan, "
        "write the Manim code to visualize it. Use clear, concise code with proper spacing. "
        "Ensure all boxes and labels are properly spaced. No SVGs. Include arrows pointing to the current code location. "
        "Write all code in full, ensuring everything is boxed and animated. "
        "Avoid overlapping elements."
    )
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions=instruction,
        input=prompt,
    )
    return response.output_text