#!/usr/bin/env python3
"""
Gyanam Automation Platform - FastAPI Server
Serves the modern UI and N8N workflow documentation system.
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import uvicorn
import os
import json
from pathlib import Path

app = FastAPI(title="Gyanam Automation Platform")

Mount static directories
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
app.mount("/workflows", StaticFiles(directory="workflows"), name="workflows")

Serve the modern homepage as default
@app.get("/", response_class=HTMLResponse)
async def homepage():
return FileResponse("frontend/modern-ui/index.html")

Health check endpoint
@app.get("/health")
async def health_check():
return {
"status": "healthy",
"message": "Gyanam Automation Platform is running",
"features": ["2,053 N8N Workflows", "Featured AI Bots", "Modern UI"]
}

Basic API endpoint for workflows
@app.get("/api/workflows")
async def get_workflows():
workflows_dir = Path("workflows")
workflows = []

text
if workflows_dir.exists():
    for file in workflows_dir.glob("*.json"):
        workflows.append({
            "name": file.stem.replace("_", " ").title(),
            "filename": file.name,
            "path": str(file)
        })

return {
    "total": len(workflows),
    "workflows": workflows[:50],  # Limit for performance
    "message": "Gyanam Automation Platform - 2,053+ N8N Workflows"
}
if name == "main":
port = int(os.environ.get("PORT", 8000))
uvicorn.run(app, host="0.0.0.0", port=port)
