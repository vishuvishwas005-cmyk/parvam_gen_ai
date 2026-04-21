# List available models

def list_openai_models():
    """List OpenAI models"""
    models = [
        "gpt-3.5-turbo",
        "gpt-4",
        "gpt-4-turbo",
        "dall-e-2",
        "dall-e-3",
        "whisper-1",
        "text-embedding-ada-002"
    ]
    return models

def list_google_models():
    """List Google AI models"""
    models = [
        "gemini-1.0-pro",
        "gemini-1.5-pro",
        "gemini-1.5-flash",
        "palm-2",
        "bert-base-uncased",
        "t5-small"
    ]
    return models

def list_huggingface_models():
    """List popular Hugging Face models"""
    models = [
        "microsoft/DialoGPT-medium",
        "facebook/blenderbot-400M-distill",
        "google/flan-t5-base",
        "openai-gpt",
        "bert-base-uncased",
        "distilbert-base-uncased"
    ]
    return models

if __name__ == "__main__":
    print("OpenAI Models:")
    for model in list_openai_models():
        print(f"  - {model}")

    print("\nGoogle AI Models:")
    for model in list_google_models():
        print(f"  - {model}")

    print("\nHugging Face Models:")
    for model in list_huggingface_models():
        print(f"  - {model}")