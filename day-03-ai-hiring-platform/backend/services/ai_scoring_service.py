def score_answer(answer):
    score = min(len(answer.split()) // 5, 10)
    return {'score': score, 'feedback': 'Add more technical details for a higher score.'}
