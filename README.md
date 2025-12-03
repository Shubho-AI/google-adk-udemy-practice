### Practice App
## Step 1
Open Windows Terminal or PowerShell as Administrator.
Run this command (one line):

>>powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"

Close and reopen your terminal after install.
Then run:
>> uv --version
## Step 2
Create a venv:
>> uv venv
## Step 3
Create a new folder [multi-agent] with __init__.py and agent.py
## Step 4
Install dependency
>> uv pip install google-adk
>> uv add litellm

























