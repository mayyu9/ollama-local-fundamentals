import ollama

response = ollama.list()

# print(response)

# chat example

res = ollama.chat(
    model="llama3.2:1b",
    messages=[
        {"role": "user", "content":"Explain how himalayas formed"}
    ]
)

print(res["message"]["content"])