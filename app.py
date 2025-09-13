# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import uuid

app = Flask(__name__)
CORS(app)  # optional if OWUI runs on a different host/port


# OpenAI-compatible: list models
@app.get("/v1/models")
def list_models():
    return jsonify(
        {
            "object": "list",
            "data": [{"id": "giga-anon-1", "object": "model", "owned_by": "500Ok"}],
        }
    )


# OpenAI-compatible: chat completions
@app.post("/v1/chat/completions")
def chat_completions():
    data = request.get_json(force=True)

    # get the last user message
    user_message = None
    for msg in reversed(data.get("messages", [])):
        if msg.get("role") == "user":
            user_message = msg.get("content")
            break

    if not user_message:
        user_message = "(no user input found)"

    return jsonify(
        {
            "id": uuid.uuid4(),
            "object": "chat.completion",
            "created": int(time.time()),
            "model": "giga-anon-1",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": f"Received message: {user_message}",
                    },
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 0, "completion_tokens": 2, "total_tokens": 2},
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
