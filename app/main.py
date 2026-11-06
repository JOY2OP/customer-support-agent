from fastapi import FastAPI

app = FastAPI(title="AI customer support")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# @app.get("/sex")
# def sex() -> dict:
#     return{"sex":"good"}