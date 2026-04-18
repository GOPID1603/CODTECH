from transformers import pipeline

def generate_text(prompt, max_len=100):
    print("Loading text generation model (GPT-2)...")
    # Using GPT-2 for text generation
    generator = pipeline("text-generation", model="gpt2")
    
    print(f"Generating continuation for: '{prompt}'...")
    # Generate text
    results = generator(prompt, max_length=max_len, num_return_sequences=1, pad_token_id=50256)
    
    return results[0]['generated_text']

if __name__ == "__main__":
    print("=== CODTECH Task 4: Generative Text Model ===")
    sample_prompt = "The future of artificial intelligence in healthcare is"
    
    generated_output = generate_text(sample_prompt, max_len=150)
    
    print("\n--- Generated Text ---\n")
    print(generated_output)
