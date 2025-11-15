import requests

API_URL = "http://0.0.0.0:8000/ask"

def ask_sherlock(question, max_tokens=200, temperature=0.7):
    payload = {
        "question": question,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    res = requests.post(API_URL, json=payload)
    res.raise_for_status()
    return res.json()["answer"]

if __name__ == "__main__":
    q = "Who is Dr. Watson?"
    print("Q:", q)
    print("A:", ask_sherlock(q))