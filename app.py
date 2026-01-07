import os
from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

app = Flask(__name__)

# Load the model and tokenizer from Hugging Face
model_name = "EleutherAI/pythia-70m"
custom_cache = r"C:\Work\Coursera\MRI\hf_cache"  # choose your directory
os.makedirs(custom_cache, exist_ok=True)


# We create a pipeline for text generation
model_pipeline = pipeline(
    "text-generation",
    model=model_name,
    torch_dtype=torch.float32,
    device=0 if torch.cuda.is_available() else -1,
    model_kwargs={"cache_dir": custom_cache}
)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        # Generate text
        result = model_pipeline(prompt, max_length=128, do_sample=True, top_k=50, top_p=0.95)
        generated_text = result[0]['generated_text']
        return render_template('index.html', user_prompt=prompt, response=generated_text)
    else:
        return render_template('index.html', user_prompt='', response='')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=os.getenv('PORT', 5000))
