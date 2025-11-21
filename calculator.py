import json
import urllib.request

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def log_operation(operation, result):
    data = json.dumps({"operation": operation, "result": result}).encode('utf-8')
    req = urllib.request.Request("https://analytics.example.com/api/log", data=data, headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req, timeout=1)
    except:
        pass
