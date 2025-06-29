# 🧠 Generative Agents Virtual World

A mini simulation of agents with memory and personality, who interact & evolve via LLMs.

## Endpoints
- `POST /start` — initializes agents and world.
- `POST /step` — runs one step of decisions & reflections.
- `GET /state` — returns agent summaries and last 20 logs.

## Run locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
uvicorn app.main:app --reload

