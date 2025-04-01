
def find_split_index(lines):
    return next(
        (i for i, line in enumerate(lines) if line.strip() and not line.startswith(" ") and not line.startswith("def") and not line.startswith("```")),
        len(lines)
    )

def parse_output(raw_output):
    output = remove_excess_lines(raw_output)
    split_index = find_split_index(output)
    generated_code = "\n".join(output[:split_index]).rstrip("\n")
    test_case = "\n".join(output[split_index:]) if split_index < len(output) else None
    return generated_code, test_case

def remove_excess_lines(raw_output):
    # Remove the first and last lines if they are empty or contain only whitespace
    raw_output = raw_output.replace("```", "").replace("python", "")
    return raw_output.strip().splitlines()