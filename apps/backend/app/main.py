from fastapi import FastAPI

app = FastAPI(
    title="Attendance Tracker API",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Attendance Tracker API is running"}
