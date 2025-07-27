#!/usr/bin
🚀 Gyanam Automation Platform - FastAPI Server
Serves the modern UI and N8N workflow documentation system.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI(title="Gyanam Automation Platform")

# Mount your new frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
app.mount("/workflows", StaticFiles(directory="workflows"), name="workflows")

# Serve the new modern homepage as the default
@app.get("/")
async def homepage():
    return FileResponse("frontend/modern-ui/index.html")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Gyanam Automation Platform is running"}

# API endpoint for workflows (basic)
@app.get("/api/workflows")
async def get_workflows():
    return {"message": "Workflows API - Coming Soon"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

