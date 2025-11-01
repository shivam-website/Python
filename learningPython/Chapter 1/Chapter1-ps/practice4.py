import os

def print_dir_contents(path='.'):
    """
    Print the names of all files and directories in the given path.
    If no path is provided, uses the current directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return

    print(f"Contents of '{path}':")
    for name in entries:
        print(name)

if __name__ == '__main__':
    # You can change '.' to any directory path you want
    print_dir_contents('.')
