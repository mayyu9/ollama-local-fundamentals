import ollama

# # Create a new model with modelfile
# modelfile = """
# FROM llama3.2:1b
# SYSTEM You are very smart assistant who knows everything about oceans. You are very succinct and informative.
# PARAMETER temperature 0.1
# """

# ollama.create(model="knowitall", modelfile=modelfile)

# res = ollama.generate(model="knowitall", prompt="why is the ocean so salty?")
# print(res["response"])

# from ollama import Client

client = ollama.Client()
response = client.create(
  model='my-assistant2',
  from_='llama3.2:1b',
  system='You are very smart assistant who knows everything about oceans. You are very succinct and informative.',
  stream=False,
)
print(response.status)

# delete model
ollama.delete("my-assistant2")
# ollama.delete("my-assistant")