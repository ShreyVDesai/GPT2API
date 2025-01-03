# Import models
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Create function
def hello_world():
    # Load pre-trained model and tokenizer from Hugging Face
    model_name = "gpt2"  
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Input prompt for the model to generate a fact
    input_prompt = "Tell me a fact:"

    # Tokenize the input prompt
    inputs = tokenizer.encode(input_prompt, return_tensors="pt")

    # Generate a creative continuation of the prompt
    output = model.generate(
        inputs,
        max_length=50, 
        num_return_sequences=1, 
        no_repeat_ngram_size=2,
        do_sample=True, 
        top_k=50, 
        top_p=0.95, 
        temperature=0.9,
        pad_token_id=tokenizer.eos_token_id  # Set pad_token_id to eos_token_id
    )

    # Decode the generated tokens back to text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Output the creative message
    print(generated_text)

# Correct the main function check
if __name__ == '__main__':
    # Call function
    hello_world()
