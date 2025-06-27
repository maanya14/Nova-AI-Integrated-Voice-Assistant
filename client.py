from openai import OpenAI

client = OpenAI(
  api_key="your_api_key"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "You are a virtual assistant JARVIS skilled in general tasks like Alexa and Google"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)
