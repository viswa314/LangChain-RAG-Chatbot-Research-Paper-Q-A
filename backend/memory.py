# Simple custom memory manager for up to 10 recent messages

chat_history = []  # global in-memory list


def add_message(role: str, content: str):
    """Append a message and trim to last 10."""
    chat_history.append({"role": role, "content": content})
    if len(chat_history) > 10:
        chat_history.pop(0)  # remove oldest


def get_memory():
    """Return the current chat history as a list of dicts."""
    return chat_history


def clear_memory():
    """Clear all stored chat history."""
    chat_history.clear()
