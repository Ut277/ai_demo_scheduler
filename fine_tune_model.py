from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

def fine_tune_model():
    # Load the tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token
    # Load and tokenize the dataset
    datasets = load_dataset('text', data_files={'train': 'data/training_data.txt'})
    tokenized_datasets = datasets.map(
        lambda examples: tokenizer(examples['text'], truncation=True, padding='max_length'),
        batched=True,
        num_proc=4  # Number of processes, adjust if necessary
    )

    # Data collator for language modeling
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False
    )

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir='finetuned_model',
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=500,
        save_total_limit=2,
    )

    # Initialize the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets['train'],
        data_collator=data_collator
    )

    # Start training
    trainer.train()
    trainer.save_model('finetuned_model')
    tokenizer.save_pretrained('finetuned_model')
if __name__ == "__main__":
    fine_tune_model()

