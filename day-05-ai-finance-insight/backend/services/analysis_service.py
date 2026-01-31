def analyze_expenses(expenses):
    total = sum(expenses)
    return {
        'total_spent': total,
        'health_score': 75 if total < 2000 else 55,
        'suggestions': 'Reduce dining out expenses and review subscriptions.'
    }
