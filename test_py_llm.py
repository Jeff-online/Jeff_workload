from transformers import pipeline , AutoTokenizer

def create_simple_llm():
    model_name='distilgpt2'
    # tokenizer= AutoTokenizer.from_pretrained(model_name)
    generator = pipeline("text-generation",model=model_name, pad_token_id=50256)
    return generator

generator= create_simple_llm()
prompt = "Once upon a time"

# generate text
generated_text = generator(prompt,max_length=100,num_return_sequences=1)
print(generated_text[0]['generated_text'])