#!/usr/bin/env python3

# /// script
# dependencies = [
#   "requests",
#   "langchain_community",
#   "langchain_core"
# ]
# ///

import glob
import base64
import argparse

import requests
from langchain_core.messages import HumanMessage
from langchain_community.chat_models import ChatOllama


model = "llava:13b" # ollama pull llava:13b
user_prompt = "Describe the contents of images in as much detail as possible."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="\n".join([
            "A simple image describing program with a multi-modal model such as llava-llama3.",
            "Use the arguments to provide either a URL or a file path",
            "The default prompt is: >>>",
            user_prompt, "<<<"
        ])
    )
    parser.add_argument("--url", "-u", required=False, help="A URL to an image to describe")
    parser.add_argument("--file", "-f", required=False, help="A filesystem path to an image to describe")
    parser.add_argument("--prompt", "-p", required=False, help="Override the default prompt")
    args = parser.parse_args()
    img_base64 = None

    if args.file:
        print(f"Describing file {args.file}...\n")
        with open(args.file, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode("utf-8")
    elif args.url:
        print(f"Describing URL {args.url}...\n")
        res = requests.get(args.url)
        res.raise_for_status()
        img_base64 = base64.b64encode(res.content).decode("utf-8")
    else:
        raise Exception("No argument provided (--url or --file)")

    if args.prompt:
        user_prompt = args.prompt

    llm = ChatOllama(
        model=model
    )
    result = llm.invoke([
        HumanMessage(
            content=[
                {"type": "text", "text": user_prompt},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{img_base64}"},
            ]
        )
    ])
    print(result.content)
    print("\n")
