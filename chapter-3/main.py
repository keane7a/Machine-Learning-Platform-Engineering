from fastapi import FastAPI 
from starlette_exporter import PrometheusMiddleware, handle_metrics
import pyjokes

app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

@app.get("/")
async def root(): 
    random_joke = pyjokes.get_joke("en", "all")
    return {"random_joke": random_joke}