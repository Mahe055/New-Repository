from openai import OpenAI

client = OpenAI()

topic = input("Enter a topic for MCQ questions: ")

prompt = f"Generate 5 multiple choice questions about {topic}. Each question should have 4 options and show the correct answer."

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nGenerated MCQs:\n")
print(response.choices[0].message.content)