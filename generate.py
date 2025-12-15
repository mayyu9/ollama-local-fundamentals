import ollama

# == Generate example ==
res = ollama.generate(
    model="llama3.2:1b",
    prompt="why is the sky blue?",
)

# show
# print(res'\n')
print(ollama.show("llama3.2:1b"))
