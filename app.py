import os
from flask import Flask, render_template, request, redirect
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

app = Flask(__name__)

#model_name = "EleutherAI/pythia-70m"
model_name = "meta-llama/Llama-3.2-1B"
custom_cache = os.path.join(os.getcwd(), "hf_cache")
os.makedirs(custom_cache, exist_ok=True)

model_pipeline = None

def try_load_pipeline():
    """Attempt to load the pipeline using an auth token if available."""
    hf_token = os.getenv("HF_API_TOKEN", None)
    if( hf_token ):
        print("Using Hugging Face token from environment variable.")    
    try:
        return pipeline(
            "text-generation",
            model=model_name,
            dtype=torch.bfloat16,
            device=0 if torch.cuda.is_available() else -1,
            model_kwargs={"cache_dir": custom_cache},
            token=hf_token if hf_token else True
        )
    except Exception as e:
        print("Failed to load pipeline:", str(e))
        return None

model_pipeline = try_load_pipeline()

@app.route('/', methods=['GET', 'POST'])
def home():
    """Check if pipeline is loaded successfully, if not redirect to the login page."""
    if model_pipeline is None:
        return redirect("https://huggingface.co/login")
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        # Generate text
        result = model_pipeline(prompt, max_new_tokens=128, do_sample=True, top_k=50, top_p=0.95)
        generated_text = result[0]['generated_text']
        return render_template('index.html', user_prompt=prompt, response=generated_text)
    else:
        return render_template('index.html', user_prompt='', response='')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=os.getenv('PORT', 5000))
