# run.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",       # Points to main.py file and app instance
        host="0.0.0.0",   # Accessible externally, use "127.0.0.1" for local only
        port=8000,
        reload=True       # Enables auto-reload on code changes
    )
