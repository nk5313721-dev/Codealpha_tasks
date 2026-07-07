import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

knowledge_base = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "what is your name": "I am an AI Chatbot created for CodeAlpha internship.",
    "how are you": "I am doing great, thank you! How are you?",
    "what is artificial intelligence": "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.",
    "bye": "Goodbye! Have a great day ahead."
}

sentences = list(knowledge_base.keys())

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input == 'bye':
        return knowledge_base['bye']
        
    sentences.append(user_input)
    vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english')
    tfidf = vectorizer.fit_transform(sentences)
    similarity_scores = cosine_similarity(tfidf[-1], tfidf[:-1])
    sentences.pop()
    
    max_score_index = similarity_scores.argsort()[0][-1]
    biggest_score = similarity_scores[0][max_score_index]
    
    if biggest_score < 0.2:
        return "I am sorry, I didn't quite understand that. Can you please rephrase?"
    else:
        matched_question = sentences[max_score_index]
        return knowledge_base[matched_question]

print("AI Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_query = input("You: ")
    if user_query.lower() == 'bye':
        print("AI Chatbot:", knowledge_base['bye'])
        break
    response = chatbot_response(user_query)
    print("AI Chatbot:", response)
