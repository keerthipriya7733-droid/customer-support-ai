# 🔍 Detect category
def detect_category(query):
    query = query.lower()

    if any(word in query for word in ["refund", "money", "cancel"]):
        return "billing"
    elif any(word in query for word in ["late", "delay", "delivery"]):
        return "delivery"
    elif any(word in query for word in ["broken", "damaged", "not working", "error", "crash"]):
        return "technical"
    else:
        return "general"


# 😊 Detect sentiment
def detect_sentiment(query):
    query = query.lower()

    if any(word in query for word in ["angry", "worst", "bad", "terrible", "hate"]):
        return "angry"
    elif any(word in query for word in ["please", "kindly"]):
        return "polite"
    else:
        return "neutral"


# 🤖 Smart decision-making agent
def simple_agent(query):
    q = query.lower()

    # Detect category
    if "refund" in q or "money" in q:
        action = "give_refund"
        reason = "Customer is asking for money back"
    elif "not working" in q or "issue" in q or "problem" in q:
        action = "ask_for_details"
        reason = "Problem is unclear, need more information"
    elif "late" in q or "delay" in q:
        action = "apologize"
        reason = "Delay issues require apology first"
    elif "thank" in q:
        action = "ignore"
        reason = "No action needed for gratitude"
    else:
        action = "ask_for_details"
        reason = "Default safe response"

    return action, reason


# 🧠 Smart feedback
def explain_feedback(query, action):
    category = detect_category(query)
    sentiment = detect_sentiment(query)

    if category == "billing" and action == "give_refund":
        return "Correct. Billing issues are best resolved with refund."
    
    elif category == "delivery" and action == "apologize":
        return "Good. Apologizing helps calm the customer."
    
    elif category == "technical" and action == "ask_for_details":
        return "Correct. Technical issues need more details."
    
    elif action == "ignore":
        return "Bad response. Ignoring customers is unacceptable."

    else:
        return "This response is okay but could be improved."


# 🤖 Generate realistic reply
def generate_reply(query, action):
    if action == "apologize":
        return "We sincerely apologize for the inconvenience. We are looking into your issue."

    elif action == "give_refund":
        return "We have processed your refund. It will reflect in your account soon."

    elif action == "ask_for_details":
        return "Could you please provide more details so we can assist you better?"

    elif action == "ignore":
        return "..."

    return "Thank you for contacting support."