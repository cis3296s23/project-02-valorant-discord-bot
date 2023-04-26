import os
import subprocess

#had to create venv and pip install all dependencies for pydocs to work with discord.py (keep this in mind if you are attempting to do this later)

#generates documentation for everything in this directory
for filename in os.listdir('.'):
    if filename.endswith('.py') and filename != 'generate_docs.py':
        module_name = filename[:-3]
        subprocess.run(["py", "-m", "pydoc", "-w", module_name], "-e", "requests", "-e", "discord.py", "-e", "discord", "-e", "BeautifulSoup4", "-e", "BS4", "-e", "bs4", "-e", "valorant")

cogs_dir = './cogs'

#generates documentation for all python files in cogs
for filename in os.listdir(cogs_dir):
    if filename.endswith('.py'):
        module_name = filename[:-3]
        subprocess.run(["py", "-m", "pydoc", "-w", f"cogs.{module_name}"], "-e", "requests", "-e", "discord.py", "-e", "discord", "-e", "BeautifulSoup4", "-e", "BS4", "-e", "bs4", "-e", "valorant")

combined_file = "pyDocumentation.html"

# Delete the combined file if it already exists
if os.path.exists(combined_file):
    os.remove(combined_file)

# Open the combined file for writing
with open(combined_file, "w") as outfile:

    # Loop through all files in the current directory
    for filename in os.listdir():
        if filename.endswith(".html"):

            # Open the file for reading and write its contents to the combined file
            with open(filename, "r") as infile:
                outfile.write(infile.read())

# Print a message when the combined file has been created
print(f"All HTML files in the current directory have been combined into {combined_file}")