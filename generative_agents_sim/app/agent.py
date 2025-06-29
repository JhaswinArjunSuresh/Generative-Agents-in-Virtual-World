from openai import OpenAI
import random

client = OpenAI()

class Agent:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.short_term_memory = []
        self.long_term_summary = f"{name} is {personality}."
    
    def observe(self, event):
        self.short_term_memory.append(event)
        if len(self.short_term_memory) > 10:
            self.short_term_memory.pop(0)
    
    def reflect(self):
        context = "\n".join(self.short_term_memory)
        prompt = f"""
Agent Summary: {self.long_term_summary}
Recent Events: {context}

Update {self.name}'s understanding of themselves and the world.
"""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": prompt}]
        )
        self.long_term_summary = response.choices[0].message.content.strip()
    
    def act(self):
        prompt = f"""
Agent: {self.name}
Summary: {self.long_term_summary}

What is {self.name} likely to do next? Respond in one sentence.
"""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": prompt}]
        )
        action = response.choices[0].message.content.strip()
        self.observe(f"{self.name} decided to {action}")
        return action

