import re

def simple_spam_classifier(text):
    text = text.lower()
    
    # Spam keywords ki list (AI Rules)
    spam_keywords = ["win", "free", "money", "prize", "click here", "lottery", "urgent", "cash", "offer"]
    
    # Check karna ki koi keyword match hota hai ya nahi
    spam_score = 0
    for keyword in spam_keywords:
        if keyword in text:
            spam_score += 1
            
    # Decision logic
    if spam_score >= 2:
        return "Spam (Dangerous/Fake Message)"
    elif spam_score == 1:
        return "Suspicious (Could be Spam)"
    else:
        return "Ham (Safe/Normal Message)"

# System ko run karne ke liye
print("--- AI Text Spam Classifier ---")
while True:
    user_msg = input("\nEnter a message to check (or type 'exit'): ")
    if user_msg.lower() == 'exit':
        break
    result = simple_spam_classifier(user_msg)
    print(f"AI Analysis Result: {result}")
