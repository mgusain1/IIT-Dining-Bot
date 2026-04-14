from datetime import datetime
from chatbot import answer_question

def run_chatbot():
    today_date = datetime.now().strftime("%Y-%m-%d")
    print("Welcome to IIT Dining Bot")
    print("Ask about breakfast, lunch, dinner, or protein items")
    print("Type 'q' to exit\n")
    while True:
        user = input("Please Insert your query")
        if user.lower() == "q":
            print("GoodBye")
            break
        answer = answer_question(user,today_date)
        print("\n" + answer + "\n")

        
if __name__ == "__main__":
    run_chatbot()