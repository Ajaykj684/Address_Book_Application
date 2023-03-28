from fastapi import FastAPI, Request
from app.api.address.endpoints import router


app = FastAPI()

app.include_router(router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    # log the request
    print(f"Received request: {request.method} {request.url}")
    for header, value in request.headers.items():
        print(f"{header}: {value}")

    response = await call_next(request)

    # log the response
    print(f"Sent response: {response.status_code}")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    return response