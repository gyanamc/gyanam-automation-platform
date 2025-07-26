import os
import sys
from pathlib import Path

# Add documentation directory to path
sys.path.append(str(Path(__file__).parent / "documentation"))

try:
    from railway_server import app
except ImportError:
    # Fallback to original run.py
    from run import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
