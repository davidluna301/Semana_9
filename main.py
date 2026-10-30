from fastapi import FastAPI, Response, Status
app = FastAPI()

@app.get("/")
def root():
    return {"status": "online","version": "1.0.0","env": "production"}

@app.get("/health")
def health_check(response: Response):
    if not IS_HEALTHY == True:
        response.status_code = Status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "unhealthy", "reason": "fallo detectado en Staging"}
    return {"status": "healthy","version": "1.0.0"}