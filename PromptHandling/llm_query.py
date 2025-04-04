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

def get_animation_DSL(prompt) -> str:
    instruction = (
            "You are converting step-by-step animation plans into a structured list of animation actions "
            "that can be rendered with Manim. Use the following format:\n\n"
            "- type: action_name\n  key1: value1\n  key2: value2\n\n"
            "Only use these action types: show_array, highlight_index, move_pointer, show_variable, update_variable, show_text.\n"
            "Use YAML syntax. Do not include any explanation."
    )
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions=instruction,
        input=prompt,
    )
    return response.output_text

def get_manim_animation_output(prompt) -> str:
    instruction = (
        "Convert the following DSL into full Manim (Python) code. "
        "Use rectangles for arrays, arrows for pointers, and Text for labels. "
        "Use self.play(...) with animations like FadeIn, Write, or Transform for every new visual element. "
        "Avoid self.add(...) unless absolutely necessary. Animate step-by-step transitions. "
        "Do not reuse positions — avoid placing multiple elements at ORIGIN. "
        "Use `.move_to(...)`, `UP`, `DOWN`, `LEFT`, `RIGHT`, or `next_to(...)` to avoid overlap. "
        "Remove or fade out old text when adding new explanatory text. "
        "Avoid ambiguous conditionals (e.g., 'if position:'); use 'if position is not None' instead. "
        "Do not include any comments or explanation. Output only valid Python Manim code."
    )
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions=instruction,
        input=prompt,
    )
    return response.output_text