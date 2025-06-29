from .agent import Agent

class VirtualWorld:
    def __init__(self):
        self.agents = []
        self.logs = []

    def setup(self):
        self.agents = [
            Agent("Alice", "curious and friendly"),
            Agent("Bob", "reserved but thoughtful"),
            Agent("Eve", "mischievous and clever")
        ]
        self.logs = ["World initialized with Alice, Bob, and Eve."]
    
    def step(self):
        for agent in self.agents:
            action = agent.act()
            log_entry = f"{agent.name}: {action}"
            self.logs.append(log_entry)
            # Share observations
            for other in self.agents:
                if other != agent:
                    other.observe(log_entry)
            agent.reflect()
    
    def get_state(self):
        return {
            "logs": self.logs[-20:],  # last 20 events
            "agents": [
                {
                    "name": a.name,
                    "summary": a.long_term_summary,
                    "recent_memory": a.short_term_memory
                }
                for a in self.agents
            ]
        }

