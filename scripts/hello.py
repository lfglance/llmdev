#!/usr/bin/env python3

import argparse

from langchain_community.llms import Ollama

model = "llama3.1"
user_prompt = "hello, how are you? tell me a joke!"
system_prompt = "you are a friendly large language model which loves to be silly and tell jokes. delight your user!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"A simple script to interact with an Ollama model of your choosing (Default {model})."
    )
    parser.add_argument("--model", "-m", required=False, help=f"The model to use and override {model}")
    parser.add_argument("--prompt", "-p", required=False, help=f"Override the default user prompt: >>>{user_prompt}<<<")
    parser.add_argument("--system", "-s", required=False, help=f"Override the default system prompt: >>>{system_prompt}<<<")
    args = parser.parse_args()

    if args.model:
        model = args.model

    if args.prompt:
        user_prompt = args.prompt

    if args.system:
        system_prompt = args.system

    llm = Ollama(
        model=model,
        system=system_prompt
    )

    result = llm.invoke(user_prompt)
    print(result)
