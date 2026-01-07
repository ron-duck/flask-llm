Flask LLM App
A simple Flask web application that loads a Hugging Face language model (e.g., EleutherAI/pythia‑70m) and generates text from a user‑provided prompt.
This README explains how to:

Install dependencies using pip + requirements.txt
Ensure the Hugging Face model downloads correctly
Run the app with app.py
Understand the cache directory behavior


1. Prerequisites
You need:

Python 3.9+
pip installed
(Optional but recommended) A virtual environment

Windows, macOS, and Linux are supported.

2. Installation
Step 1 — Clone or download the project
Shellgit clone <your-repo-url>cd <your-project-folder>Show more lines
Step 2 — Create and activate a virtual environment (recommended)
Windows (PowerShell)
PowerShellpython -m venv venv.\venv\Scripts\activateShow more lines
macOS/Linux
Shellpython3 -m venv venvsource venv/bin/activateShow more lines
Step 3 — Install dependencies using requirements.txt
Shellpip install -r requirements.txtShow more lines
This installs:

Flask
transformers
torch (CPU or CUDA version depending on your environment)
huggingface_hub
Any other required packages


3. Model Cache Directory
Your app currently sets the Hugging Face cache directory inside the current working directory, for example:
./hf_cache/

When the app runs for the first time, Hugging Face will download:

model weights
tokenizer files
config.json

into this directory.
This avoids using the default path:
C:\Users\<username>\.cache\huggingface\


4. Running the Flask App
Once dependencies are installed, simply run:
Shellpython app.pyShow more lines
You should see output like:
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit

Open your browser to:
http://127.0.0.1:5000

You’ll see a text box where you can enter a prompt, and the model will generate output.
