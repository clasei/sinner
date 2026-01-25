#!/usr/bin/env python3
"""Quick diagnostic tool for LM Studio connection."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1")
API_KEY = os.getenv("LMSTUDIO_API_KEY", "lm-studio")
MODEL_ID = os.getenv("MODEL_ID", "google/gemma-3n-e4b")

print("=" * 60)
print("LM Studio Connection Diagnostic")
print("=" * 60)

print(f"\n1. Configuration:")
print(f"   Base URL: {BASE_URL}")
print(f"   Model ID: {MODEL_ID}")
print(f"   API Key: {API_KEY[:10]}...")

print(f"\n2. Testing server connection...")
try:
    resp = requests.get(f"{BASE_URL}/models", timeout=5)
    resp.raise_for_status()
    models = resp.json()
    print(f"   ✓ Server is running")
    print(f"   Available models: {len(models.get('data', []))}")
    for model in models.get('data', []):
        print(f"     - {model['id']}")
except requests.exceptions.ConnectionError:
    print(f"   ✗ Cannot connect to {BASE_URL}")
    print(f"   Is LM Studio running?")
    exit(1)
except Exception as e:
    print(f"   ✗ Error: {e}")
    exit(1)

print(f"\n3. Testing chat completion with model: {MODEL_ID}")
try:
    payload = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": "Say 'hello' in one word"}],
        "temperature": 0.7,
        "max_tokens": 10
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    resp = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json=payload,
        timeout=30
    )
    
    if resp.status_code == 200:
        result = resp.json()
        message = result['choices'][0]['message']['content']
        print(f"   ✓ Model responded: '{message.strip()}'")
        print(f"\n🎾 Everything works! sinner is ready to use.")
    else:
        print(f"   ✗ Model error: {resp.status_code}")
        print(f"   Response: {resp.text}")
        print(f"\n💡 Solution:")
        print(f"   1. Open LM Studio")
        print(f"   2. Go to the Chat tab")
        print(f"   3. Load a model by clicking 'Select a model'")
        print(f"   4. Make sure the model name matches: {MODEL_ID}")
        print(f"   5. Or update MODEL_ID in .env to match your loaded model")
        
except requests.exceptions.Timeout:
    print(f"   ✗ Request timeout (model might be loading...)")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n" + "=" * 60)
