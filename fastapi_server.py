# fastapi_server.py
from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.post("/start/{receiver_name}")
async def start_receiver(receiver_name: str):
    try:
        subprocess.Popen(["python3", "receiver_service.py", receiver_name])
        return {"status": "started", "receiver": receiver_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



