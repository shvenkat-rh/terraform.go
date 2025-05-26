# go_bridge.py
import ctypes
import os
# Path to your shared library
# It's good practice to make this configurable or use an absolute path
# if the module will be used from different locations.
# For simplicity, we'll keep the hardcoded path from your example.
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#SO_FILE_PATH = os.path.join(BASE_DIR, 'list.so')
SO_FILE_PATH= '/tmp/list.so'


def call_crud_project():
    """
    Loads the Go shared library and calls the ManageProject function.
    Returns the string result from the Go function.
    """
    try:
        lib = ctypes.cdll.LoadLibrary(SO_FILE_PATH)
        print(f"Loaded shared library: {SO_FILE_PATH}")

        # Set the restype for the function
        lib.ManageProject.restype = ctypes.c_char_p

        # Call the Go function
        result_ptr = lib.ManageProject()

        # Decode the C string pointer to a Python string
        result_str = result_ptr.decode('utf-8')
        return result_str
    except OSError as e:
        print(f"Error loading or calling shared library: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# You can add a test block to run this directly if needed
if __name__ == '__main__':
    project_data = call_crud_project()
    if project_data:
        print("Data from Go (ManageProject):", project_data)
