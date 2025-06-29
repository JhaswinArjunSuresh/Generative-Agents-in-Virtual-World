from fastapi import FastAPI
from .world import VirtualWorld

app = FastAPI()
world = VirtualWorld()

@app.post("/start")
def start():
    world.setup()
    return {"status": "simulation started"}

@app.post("/step")
def step():
    world.step()
    return {"state": world.get_state()}

@app.get("/state")
def state():
    return world.get_state()

