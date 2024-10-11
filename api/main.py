from api import app
from .routes import home
from dotenv import load_dotenv

load_dotenv()
app.include_router(home.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)