from fetch_menu import get_today_date
from chatbot import answer_question

def run_chatbot():
    today_date = get_today_date()
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