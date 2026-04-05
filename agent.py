def simple_agent(query):
    query = query.lower()

    # 🔹 Delivery issues
    if "where" in query or "late" in query or "delayed" in query or "not arrived" in query:
        return "ask_for_details", "Customer is asking about delivery status"

    # 🔹 Refund / Payment issues
    elif "refund" in query or "money" in query or "charged" in query or "payment" in query:
        return "give_refund", "Customer has a refund or payment issue"

    # 🔹 Product issues
    elif "damaged" in query or "broken" in query or "wrong item" in query:
        return "ask_for_details", "Product issue needs more details"

    # 🔹 Complaint / Angry tone
    elif "bad" in query or "terrible" in query or "frustrated" in query or "angry" in query:
        return "apologize", "Customer is expressing frustration"

    # 🔹 App / technical issues
    elif "app" in query or "crash" in query or "error" in query:
        return "ask_for_details", "Technical issue requires investigation"

    # 🔹 Default fallback
    else:
        return "ask_for_details", "General query, more details required"