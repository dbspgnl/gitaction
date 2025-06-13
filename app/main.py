from fastapi import FastAPI

app = FastAPI(
    title="Vendors FastAPI",
    version="1.0.0",
    description="Vendors Management System API"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/test")
async def test():
    return {"result": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)