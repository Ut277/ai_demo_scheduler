# response_generator.py

from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate_response(prompt):
    print(f"Generating response for prompt: {prompt}")
    try:
        tokenizer = GPT2Tokenizer.from_pretrained('finetuned_model')
        model = GPT2LMHeadModel.from_pretrained('finetuned_model')
        print("Model and tokenizer loaded.")

        inputs = tokenizer.encode(prompt, return_tensors='pt')
        outputs = model.generate(inputs, max_length=50, do_sample=True)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Generated response: {response}")
        return response
    except Exception as e:
        print(f"An error occurred during response generation: {e}")
        return ""

if __name__ == "__main__":
    # Test the generate_response function independently
    test_prompt = "Tell me about the ERP system."
    generate_response(test_prompt)


# from transformers import GPT2Tokenizer, GPT2LMHeadModel

# def generate_response(prompt):
#     print(f"Generating response for prompt: {prompt}")
#     try:
#         # Load GPT-2 model and tokenizer
#         tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#         model = GPT2LMHeadModel.from_pretrained('gpt2')

#         # Set the pad token explicitly
#         tokenizer.pad_token = tokenizer.eos_token
#         model.config.pad_token_id = tokenizer.pad_token_id  # Ensure padding token is recognized

#         print("Model and tokenizer loaded.")

#         # Tokenize input with padding and truncation
#         inputs = tokenizer(prompt, return_tensors='pt', padding=True, truncation=True)

#         # Generate response
#         outputs = model.generate(
#             inputs['input_ids'],
#             attention_mask=inputs['attention_mask'],  # Ensure attention mask is set
#             max_length=50,
#             do_sample=True
#         )
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#         print(f"Generated response: {response}")
#         return response
#     except Exception as e:
#         print(f"An error occurred during response generation: {e}")
#         return ""

# if __name__ == "__main__":
#     test_prompt = "Tell me about the ERP system."
#     generate_response(test_prompt)



