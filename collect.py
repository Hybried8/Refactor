import os

def collect_code_samples(directory):
    code_samples = []
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                code = file.read()
                code_samples.append(code)
    return code_samples
