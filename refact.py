import ast

def rename_variables(code, old_name, new_name):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return None, str(e)

    def rename_variable(node):
        if isinstance(node, ast.Name) and node.id == old_name:
            node.id = new_name

    ast.walk(tree, rename_variable)

    # Generate refactored code
    refactored_code = ast.unparse(tree)
    return refactored_code, None

if __name__ == "__main__":
    # Sample Python code for testing
    python_code = """
    def calculate_area(radius):
        pi = 3.14
        return pi * radius * radius

    circle_radius = 5
    result = calculate_area(circle_radius)
    print("The area of the circle is:", result)
    """

    old_variable_name = "radius"
    new_variable_name = "r"

    refactored_code, error = rename_variables(python_code, old_variable_name, new_variable_name)

    if error:
        print("Error:", error)
    else:
        print("Refactored Code:")
        print(refactored_code)
