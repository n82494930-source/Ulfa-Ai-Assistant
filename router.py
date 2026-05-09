def route(user_input):
    text = user_input.lower()

    # JOBS
    if "job" in text:
        return "jobs"

    # ROTA
    elif "rota" in text or "shift" in text or "work" in text:
        return "rota"

    # DE COACH
    elif any(word in text for word in ["sql", "python", "loop", "joins"]):
        return "de_coach"

    # DEFAULT → AI
    else:
        return "ai"