import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data import faq_data

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))


def preprocess(text):
    tokens = word_tokenize(text.lower())
    return " ".join([word for word in tokens if word.isalnum() and word not in stop_words])

# Prepare the data
questions = [preprocess(faq["question"]) for faq in faq_data]
answers = [faq["answer"] for faq in faq_data]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


def get_response(user_input):
    user_input_processed = preprocess(user_input)
    user_vec = vectorizer.transform([user_input_processed])
    similarity = cosine_similarity(user_vec, question_vectors)
    best_match_idx = similarity.argmax()
    
    if similarity[0, best_match_idx] > 0.2:
        return answers[best_match_idx]
    else:
        return "Sorry, I don't understand that."
    
# Main loop
print("Hi! Ask me anything. Type 'exit' to quit.")
while True:
    user_input = input("You : ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    print("Bot:", get_response(user_input))