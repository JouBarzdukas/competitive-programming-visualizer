import openai

def get_LLM_response(prompt) -> str:
    response = openai.responses.create(
        model="gpt-4o-mini",
        instructions="Write the python code for the following problem which starts at def and ends at the return statement. This should have NO comments. After that, write potential variables for a generic case in one line. For example, if a function had three parameters, this COULD be a correct choice: ""var1 = [3,5,1,6,7,1,2], var2 = [3,2,8,1], k = 3"". Do not include any explanation.",
        input=prompt,
    )
    return response.output_text