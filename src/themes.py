# src/themes.py
def assign_theme(nouns):
    theme_mapping = {
        "User Interface & Experience": ["ui", "design", "experience", "user", "application", "app"],
        "Account Access Issues": ["access", "account", "password", "pin"],
        "Transaction Performance": ["transfer", "transaction", "money", "bill", "balance"],
        "Customer Support": ["service", "developer", "help", "thank", "super"],
        "Feature Requests / Updates": ["update", "feature", "option", "system", "mode"]
    }
    assigned = []
    for theme, words in theme_mapping.items():
        if any(word in nouns for word in words):
            assigned.append(theme)
    if not assigned:
        assigned.append("Other")
    return ", ".join(assigned)
