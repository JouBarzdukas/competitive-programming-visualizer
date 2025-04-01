import openai

def get_coding_LLM_response(prompt) -> str:
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions="Write the python code for the following problem which starts at def and ends at the return statement. This should have NO comments. After that, write potential variables for a generic case in one line. For example, if a function had three parameters, this COULD be a correct choice: ""var1 = [3,5,1,6,7,1,2], var2 = [3,2,8,1], k = 3"". However, use the same variable names as the ones in the example: if def method(s), you should use write ""s = "" in the test case. Do not include any explanation.",
        input=prompt,
    )
    return response.output_text

def get_step_by_step_instructions(prompt) -> str:
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions="Suppose you are an animator's assistant which specialises in education. You are tasked with writing code which shows exactly what is going on given a method and some test variables. The animator needs you to give step by step instructions on what digital movements should be going on to best make this animation work. By that, I mean you should state EXACTLY what should be happening at each step and telling me HOW it should be animated. Start each step with ""Step X:"" where X is the step number.",
        input=prompt,
    )
    return response.output_text
def get_manim_animation_output(prompt) -> str:
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions="Write the manim code for the following problem. To ensure proper animation style, all boxes should be properly spaced from each other and all labels should also be properly spaced.",
        input=prompt,
    )
    return response.output_text