import json

response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

parsed = json.loads(response)
print("Req id: ", parsed["id"])
print("Status: ", parsed["status"])
print("Result text: ", parsed["result"]["text"])
print(f"Confidence : {parsed["result"]["confidence"]}" if parsed["result"]["confidence"] > 0.9 else "Warning: low confidence score")

result = {
        "success": True, 
        "income":4.2,
        "age":23
}



with open("response.json", "w") as fileHandler:
    json.dump(result, fileHandler)
    json.dump(parsed, fileHandler)