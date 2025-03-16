# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hJMVUEr1hnxa2moAD0c-0qUQhKPBVYqA
"""

import requests
import json

# Replace with YOUR GROQ API key
API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

import json
import requests

# ✅ API Configuration
API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# ✅ Load the FAQ JSON Data
faq_data = {
    "faqs": [
        {
            "question": "What documents are required to open a Current Account?",
            "answer": "To open a Current Account, you need: Proof of Identity (PAN, Aadhar, Passport), Proof of Address (Utility bill, Rent agreement), Business Registration Certificate, and a filled account opening form."
        },
        {
            "question": "Can I transfer my Current Account to another branch?",
            "answer": "Yes, you can transfer your Current Account to another branch. Visit your bank branch and submit a written request along with your account details."
        },
        {
            "question": "What is the minimum balance for a Regular Current Account?",
            "answer": "The minimum balance required for a Regular Current Account is Rs. 10,000 as an Average Quarterly Balance (AQB)."
        },
        {
            "question": "How can I access my account through NetBanking?",
            "answer": "You can log in using your Customer ID and NetBanking password. If you forget your password, use the 'Forgot Password' option to reset it."
        },
        {
            "question": "How do I update my PAN details in my account?",
            "answer": "You can update your PAN details via NetBanking or by visiting the nearest branch with a copy of your PAN card."
        },
        {
            "question": "What is the processing time for outstation cheque clearance?",
            "answer": "For metro locations, it takes 7 working days. For other state capitals, it takes up to 10 working days, and for non-metro locations, up to 14 working days."
        },
        {
            "question": "What is the penalty for premature Fixed Deposit closure?",
            "answer": "A penalty of 1% of the applicable interest rate is charged for premature Fixed Deposit closure."
        },
        {
            "question": "Can I access my account through PhoneBanking?",
            "answer": "Yes, PhoneBanking allows you to check account details, request statements, inquire about interest rates, and request cheque books."
        },
        {
            "question": "Is it necessary to open separate Current Accounts for different branches?",
            "answer": "No, a Premium Current Account allows you to manage multiple locations under a single account."
        },
        {
            "question": "How do I apply for a business loan?",
            "answer": "You need to provide financial statements, a business plan, and KYC documents. You can apply online or visit a branch."
        }
    ]
}

# ✅ Function to check FAQ before calling Groq API
def check_faq(question):
    for faq in faq_data["faqs"]:
        if question.lower() in faq["question"].lower():  # Case-insensitive match
            return faq["answer"]
    return None  # Return None if no match is found

# ✅ Function to get a response from Groq API if FAQ doesn't have the answer
def get_groq_response(messages, model="deepseek-r1-distill-llama-70b"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "messages": messages,
    }
    response = requests.post(API_URL, headers=headers, json=data)

    # ✅ Handle potential API errors
    try:
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# ✅ Chatbot with memory (includes FAQ search)
def chatbot_with_memory():
    messages = []
    print("Welcome to the Bank FAQ Chatbot! Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        # ✅ Check if answer exists in FAQ
        faq_answer = check_faq(user_input)
        if faq_answer:
            print("Chatbot (FAQ):", faq_answer)
            continue  # Skip calling Groq API if FAQ has the answer

        # ✅ If no FAQ match, use Groq API
        messages.append({"role": "user", "content": user_input})
        response = get_groq_response(messages)

        if response:
            print("Chatbot (AI):", response)
            messages.append({"role": "assistant", "content": response})
        else:
            print("Sorry, I couldn't generate a response.")

# ✅ Run the chatbot
if __name__ == "__main__":
    chatbot_with_memory()