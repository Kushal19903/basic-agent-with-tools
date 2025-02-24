import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "basic-agent-with-tool"

list_of_files = [
    "src/__init__.py",
    "src/agent.py",
    "src/tools.py",
    "src/utils.py",
    "tests/test_agent.py",
    "scripts/run_agent.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "OAI_CONFIG_LIST.json"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
