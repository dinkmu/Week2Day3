import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from the .env file
# This automatically turns on LangSmith tracing and authenticates OpenAI
load_dotenv()

# Initialize the model using ChatOpenAI as required
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Three distinct prompts designed to show variance in token counts and latency
prompts = [
    "What is 2 + 2?",
    "Explain the concept of quantum computing in two sentences.",
    "Write a detailed, step-by-step beginner's guide on how to bake sourdough bread from scratch, including exact ingredients, fermentation schedules, and troubleshooting tips."
]

print(f"🚀 Running project: {os.getenv('LANGSMITH_PROJECT')}")
print("=" * 60)

# Iterate through prompts, invoke the model, and print results
for i, p in enumerate(prompts, start=1):
    print(f"\n[Run {i}] Sending prompt: \"{p[:40]}...\"")
    
    response = llm.invoke(p)
    
    print(f"Answer: {response.content[:100]}...\n" + "-" * 60)

print("\n✨ All runs completed! Check your dashboard at smith.langchain.com")