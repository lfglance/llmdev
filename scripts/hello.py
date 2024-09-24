#!/usr/bin/env python3

from langchain_community.llms import Ollama

model = "llama3.1"
user_prompt = "hello, how are you? tell me a joke!"
system_prompt = "you are a friendly large language model which loves to be silly and tell jokes. delight your user!"

if __name__ == "__main__":
    llm = Ollama(
        model=model,
        system=system_prompt
    )
    result = llm.invoke("hello, how are you? tell me a joke!")
    print(result)
