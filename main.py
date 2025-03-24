import getpass
import os

def main():
    print("Welcome to the main program!")

if __name__ == "__main__":
    main()

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = "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" #getpass.getpass("Enter API Key: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("llama3-8b-8192", model_provider="groq")
response = model.invoke("first person to land on the moon")
print(response.content)