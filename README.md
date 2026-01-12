📘 Flask LLM App
A simple Flask web application that loads a Hugging Face language model (e.g., **EleutherAI/pythia‑70m**) and generates text from a user‑provided prompt.

This README explains how to:

- Install dependencies using **pip** + `requirements.txt`  
- Ensure the Hugging Face model downloads correctly  
- Run the app with `app.py`  
- Understand the cache directory behavior  

---

## 🛠️ 1. Prerequisites

You need:

- **Python 3.9+**
- **pip** installed
- (Optional but recommended) A **virtual environment**

Windows, macOS, and Linux are supported.

---

## 📦 2. Installation

### **Step 1 — Clone or download the project**
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### **Step 2 — Create and activate a virtual environment (recommended)**

#### **Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

#### **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **Step 3 — Install dependencies using requirements.txt**

```bash
pip install -r requirements.txt
```

This installs:

- Flask  
- transformers  
- torch (CPU or CUDA version depending on your environment)  
- huggingface_hub  
- Any other required packages  

---

## 📁 3. Model Cache Directory

Your app sets the Hugging Face cache directory inside the **current working directory**, for example:

```
./hf_cache/
```

When the app runs for the first time, Hugging Face will download:

- model weights  
- tokenizer files  
- config.json  

into this directory.

This avoids using the default path which would not be picked up in a scan of the source directory:
```
C:\Users\<username>\.cache\huggingface\
```

---

## ▶️ 4. Running the Flask App

Once dependencies are installed, run:

```bash
python app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Open your browser to:
```
http://127.0.0.1:5000
```

You’ll see a text box where you can enter a prompt, and the model will generate output.

---

## 🔍 5. Common Issues & Tips

### **Corporate Proxy / SSL Issues**
If you are behind Zscaler or any SSL‑interception proxy, you may get errors such as:

```
SSLCertVerificationError
```

Fixes include:
- Disabling the proxy (temporary)  
- Adding your corporate root CA to the Python certificate store  
- Pre‑downloading the model and using offline mode

## 🔑 6. Accessing Gated Hugging Face Models
If you want to use gated or private Hugging Face models, set an environment variable named `HF_TOKEN` with your personal token from Hugging Face (e.g. from https://huggingface.co/settings/tokens) before running the app:

```bash
$ set HF_TOKEN=hf_xxxYOURTOKENxxx
$ python app.py
```

This lets the libraries authenticate and download restricted model weights. **Important**: Keep the token safe and avoid committing it to source control.

## 🔑 6. Accessing Gated Hugging Face Models
If you want to use gated or private Hugging Face models, set an environment variable named `HF_TOKEN` with your personal token from Hugging Face (e.g. from https://huggingface.co/settings/tokens) before running the app:

```bash
$ set HF_TOKEN=hf_xxxYOURTOKENxxx
$ python app.py
```

This lets the libraries authenticate and download restricted model weights. **Important**: Keep the token safe and avoid committing it to source control.

## 🔑 6. Accessing Gated Hugging Face Models
If you want to use gated or private Hugging Face models, set an environment variable named `HF_TOKEN` with your personal token from Hugging Face (e.g. from https://huggingface.co/settings/tokens) before running the app:

```bash
$ set HF_TOKEN=hf_xxxYOURTOKENxxx
$ python app.py
```

This lets the libraries authenticate and download restricted model weights. **Important**: Keep the token safe and avoid committing it to source control.