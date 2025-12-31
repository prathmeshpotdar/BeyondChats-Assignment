import requests
import json
import sys

# Configuration
API_URL = "http://127.0.0.1:8000/api/articles"
SOURCE_URL = "https://beyondchats.com/blogs/"

def force_seed():
    print(f"--- STARTING SEED PROCESS ---")
    print(f"Target API: {API_URL}")

    # 1. Attempt to Connect to API first
    try:
        r = requests.get(API_URL)
        print(f"API Connection Check: Status {r.status_code}")
    except Exception as e:
        print(f"CRITICAL ERROR: Cannot connect to Laravel API. Is it running?")
        print(f"Error details: {e}")
        sys.exit(1)

    # 2. Define a Manual Test Article (The Failsafe)
    manual_article = {
        "title": "What is Chatbot Architecture?",
        "original_content": "Chatbot architecture refers to the structural design of a conversational AI. It includes the NLU engine, dialog manager, and integration layers. This is a manual test entry to ensure the system works.",
        "source_url": "https://beyondchats.com/blogs/test-entry"
    }

    # 3. Send to Database
    print(f"\nAttempting to insert test article...")
    try:
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post(API_URL, json=manual_article, headers=headers)
        
        if response.status_code in [200, 201]:
            print(f"SUCCESS! Article inserted successfully.")
            print(f"Response: {response.json()}")
        else:
            print(f"FAILED to insert article.")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")
            
    except Exception as e:
        print(f"Error sending data: {e}")

if __name__ == "__main__":
    force_seed()