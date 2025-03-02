import os

def path(file_name):
    """Returns the absolute path to a resource file."""

    # Get the directory of the current file (resource.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the resources directory, assuming it's located in the tests folder
    resource_path = os.path.join(current_dir, '..', '..','Part2', 'tests', 'resources', file_name)

    # Convert to an absolute path for robustness
    absolute_path = os.path.abspath(resource_path)

    print(f"Resource path: {absolute_path}")  # Add this line for debugging
    return absolute_path