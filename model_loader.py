from dotenv import load_dotenv
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

# Load Hugging Face API key (optional)
load_dotenv()
hf_api_key = os.getenv("HUGGINGFACE_API_KEY")
print("Hugging Face Key:", hf_api_key if hf_api_key else "Not Found")

# Model ID
model_id = "google/flan-t5-base"

# Use GPU if available
device = 0 if torch.cuda.is_available() else -1
print(f" Running on {'GPU' if device == 0 else 'CPU'}")

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# Create pipeline
pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    device=device
)

# Wrapper class for calling the pipeline
class SimpleWrapper:
    def __init__(self, pipe): 
        self.pipe = pipe  

    def invoke(self, prompt):
        result = self.pipe(prompt)
        return result[0]["generated_text"].strip()

# Instantiate the wrapper
rf = SimpleWrapper(pipe)
