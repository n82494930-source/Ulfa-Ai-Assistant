from ai import ask_ai
from jobs import get_jobs
from rota import get_today_rota
from de_coach import explain
from smart_router import route
from notifier import notify
from jobs import get_new_jobs



while True:
    user = input("You: ")

    intent = route(user)

    if intent == "jobs":
        print(get_jobs())

    elif intent == "rota":
        print(get_today_rota())

    elif intent == "de_coach":
        if "sql" in user.lower():
            print(explain("sql"))
        elif "python" in user.lower():
            print(explain("python"))
        else:
            print(ask_ai(user))

    else:
        print(ask_ai(user))