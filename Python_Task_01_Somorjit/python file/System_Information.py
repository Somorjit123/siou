import os
import platform
import sys
os_name = platform.system()
username = os.getlogin()
current_directory = os.getcwd()
python_version = sys.version
print("Operating System:", os_name)
print("Username:", username)
print("Current Working Directory:", current_directory)
print("Python Version:", python_version)