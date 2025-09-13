from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Sample data with multiple chat sessions
data = [
    {
        "id": "chat-12345",
        "chat_id": "chat-12345",
        "chat_name": "Linux Crash Course",
        "user_id": "user-001",
        "created_at": "2025-09-11T17:45:00Z",
        "messages": [
            {
                "timestamp": "2025-09-11T17:45:10Z",
                "role": "user",
                "message": "Hello AI, how are you?"
            },
            {
                "timestamp": "2025-09-11T17:45:12Z",
                "role": "ai",
                "message": "I’m doing great! How can I help you today?"
            },
            {
                "timestamp": "2025-09-11T17:46:00Z",
                "role": "user",
                "message": "Can you explain what Linux is?"
            },
            {
                "timestamp": "2025-09-11T17:46:05Z",
                "role": "ai",
                "message": "Linux is an open-source operating system based on Unix. It is widely used for servers, desktops, and embedded systems."
            },
            {
                "timestamp": "2025-09-11T17:47:00Z",
                "role": "user",
                "message": "How do I list files in a directory?"
            },
            {
                "timestamp": "2025-09-11T17:47:05Z",
                "role": "ai",
                "message": "You can use the 'ls' command to list files in a directory."
            }
        ]
    },
    {
        "id": "chat-67890",
        "chat_id": "chat-67890",
        "chat_name": "Python Basics",
        "user_id": "user-002",
        "created_at": "2025-09-12T10:00:00Z",
        "messages": [
            {
                "timestamp": "2025-09-12T10:00:10Z",
                "role": "user",
                "message": "What is a variable in Python?"
            },
            {
                "timestamp": "2025-09-12T10:00:12Z",
                "role": "ai",
                "message": "A variable in Python is a container for storing data values."
            },
            {
                "timestamp": "2025-09-12T10:01:00Z",
                "role": "user",
                "message": "How do I print something?"
            },
            {
                "timestamp": "2025-09-12T10:01:05Z",
                "role": "ai",
                "message": "You can use the print() function to display output."
            }
        ]
    },
    {
        "id": "chat-54321",
        "chat_id": "chat-54321",
        "chat_name": "Docker Introduction",
        "user_id": "user-003",
        "created_at": "2025-09-13T09:30:00Z",
        "messages": [
            {
                "timestamp": "2025-09-13T09:30:10Z",
                "role": "user",
                "message": "What is Docker?"
            },
            {
                "timestamp": "2025-09-13T09:30:12Z",
                "role": "ai",
                "message": "Docker is a platform for developing, shipping, and running applications in containers."
            },
            {
                "timestamp": "2025-09-13T09:31:00Z",
                "role": "user",
                "message": "How do I start a container?"
            },
            {
                "timestamp": "2025-09-13T09:31:05Z",
                "role": "ai",
                "message": "You can use 'docker run' to start a container."
            }
        ]
    }
]


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
