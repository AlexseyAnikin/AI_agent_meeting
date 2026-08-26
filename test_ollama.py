import ollama

response = ollama.chat(
    model="qwen3:14b",
    messages=[
        {
            "role": "user",
            "content": "Назови столицу России одним словом"
        }
    ]
)

print(response)