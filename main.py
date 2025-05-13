#!/usr/bin/env -S uv run --script

import subprocess
from dotenv import load_dotenv

load_dotenv()

prompt = "You are a software engineer. First git checkout a new branch. CREATE a todo.py: a minimal cli todo application. Then commit your changes."

command = ["codex", "--approval-mode", "full-auto", prompt]

subprocess.run(command, check=True)
