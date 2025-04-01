import openai

def get_LLM_response(prompt) -> str:
    response = openai.responses.create(
        model="gpt-4o",
        instructions="You are a coding assistant that talks like a pirate.",
        input="prompt",
    )
    return response.output_text