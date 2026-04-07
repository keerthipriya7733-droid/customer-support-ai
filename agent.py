def simple_agent(query):
    query = query.lower()

    score_map = {
        "refund": ["refund", "money", "charged", "payment"],
        "delivery": ["where", "late", "delayed", "not arrived"],
        "product": ["damaged", "broken", "wrong item"],
        "complaint": ["bad", "terrible", "frustrated", "angry"],
        "technical": ["app", "crash", "error"]
    }

    scores = {k: 0 for k in score_map}

    for category, keywords in score_map.items():
        for word in keywords:
            if word in query:
                scores[category] += 1

    best_category = max(scores, key=scores.get)

    if best_category == "refund":
        return "give_refund", "Detected refund/payment issue"
    elif best_category == "delivery":
        return "ask_for_details", "Delivery issue detected"
    elif best_category == "product":
        return "ask_for_details", "Product issue needs clarification"
    elif best_category == "complaint":
        return "apologize", "Customer is unhappy"
    elif best_category == "technical":
        return "ask_for_details", "Technical issue detected"
    else:
        return "ask_for_details", "General query"
