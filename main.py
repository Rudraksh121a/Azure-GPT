from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Sample data
data = {
    "searches": [
        {
            "timestamp": "2023-10-01T12:00:00Z",
            "id": "example1",
            "chatname": "Chat 1",
            "chaturl": "http://example.com/chat1",
            "conversation": [
                {"role": "user", "message": "hi"},
                {"role": "system", "message": "how can I help you?"},
                {"role": "user", "message": "hi"},
                {"role": "system", "message": "how can I help you?"}
            ]
        },
        {
            "id": "example2",
            "chatname": "Chat 2",
            "chaturl": "http://example.com/chat2",
            "conversation": [
                {"role": "user", "message": "hello"},
                {"role": "system", "message": "welcome!"}
            ]
        },
        {
            "id": "example3",
            "conversation": [
                {"role": "user", "message": "what's the weather?"},
                {"role": "system", "message": "It's sunny today."}
            ]
        }
    ]
}

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
