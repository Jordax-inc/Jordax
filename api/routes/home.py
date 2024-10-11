import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from langchain_openai import OpenAI
from langchain import hub
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from langchain.prompts import PromptTemplate

load_dotenv()

router = APIRouter()

# Set up Jinja2 templates
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI language model with the API key
llm = OpenAI(api_key=api_key)

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/chat")
async def chat(request: Request):
    try:
        # Get the user's message from the query parameters
        user_message = request.query_params.get("message", "")

        # Pull the prompt from LangChain Hub
        prompt = hub.pull("white-rabbit")
        if isinstance(prompt, PromptTemplate):
            formatted_prompt = prompt.format(user_input=user_message)
        else:
            formatted_prompt = f"{str(prompt)} {user_message}"

        response = llm.invoke(formatted_prompt)

        return JSONResponse(content={"response": response})
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return JSONResponse(content={"error": str(e)}, status_code=500)