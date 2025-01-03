


# GPT-2 Text Generation Project

## Project Overview
This application demonstrates the use of OpenAI’s GPT-2 model from Hugging Face Transformers for generating creative text based on input prompts. The project includes two Python scripts:
- `app.py`: Generates a fact.
- `hello_world.py`: Generates a creative way to say "Hello World".

## Requirements
- Python 3.6 or later
- `transformers` library from Hugging Face
- `torch` library

### Installation
To install the necessary dependencies, run:
```bash
pip install transformers torch
```

## Setup Instructions
1. Clone the project repository:
   ```bash
   git clone https://github.com/ShreyVDesai/GPT2API.git
   cd GPT2API
   ```
2. Install required dependencies using the command above in a new environment.
3. Run either of the Python scripts with:
   ```bash
   python app.py
   ```
   Or:
   ```bash
   python hello_world.py
   ```

## Code Overview
### Model Loading
Both scripts load the GPT-2 model and tokenizer from the Hugging Face library:
```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
```
This initializes the model and tokenizer required for generating text.

### Text Generation
The model generates creative responses based on input prompts. The `generate` method uses various parameters to control the randomness and diversity of outputs:
- **`max_length`**: Limits the length of generated text.
- **`num_return_sequences`**: Specifies the number of unique responses to generate.
- **`top_k`** and **`top_p`**: Control the sampling process for more creative outputs.
- **`temperature`**: Affects randomness (higher values mean more randomness).

### Functionality
Each script includes a `hello_world` function that:
1. Accepts a prompt.
2. Tokenizes the prompt.
3. Generates output text, which is then printed to the console.

For example, in `app.py`, the input prompt is:
```python
input_prompt = "Tell me a fact:"
```
The generated output might be:
> The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the metal.

## Reflection
Working with generative AI models such as GPT-2 provided valuable insights into text generation and creative output generation using AI. 

### Challenges
- Adjusting model parameters (`top_k`, `top_p`, `temperature`) to balance creativity and coherence. For instance, an initially high `temperature` led to incoherent outputs, prompting experimentation.
- Handling tokenization and model loading using the Hugging Face Transformers library.
- Dealing with unexpected model results, requiring refined input prompts and iterations to improve outputs.

### Learnings
- Gained a deeper understanding of prompt engineering and generative AI principles.
- Improved skills in using large language models for practical applications.

### Future Work
- Build more complex, user-interactive applications such as chatbots or storytelling generators.
- Explore fine-tuning techniques to adapt GPT-2 to niche topics for targeted outputs.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
