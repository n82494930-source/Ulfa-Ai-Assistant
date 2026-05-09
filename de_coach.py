def explain(topic):
    try:
        with open(f"data/{topic}.txt") as f:
            return f.read()
    except FileNotFoundError:
        return "Sorry, I don’t have notes for that topic yet."


        