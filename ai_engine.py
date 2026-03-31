from textblob import TextBlob
import random

def generate_question(interview_type):
    hr_questions = [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths and weaknesses?",
        "Where do you see yourself in 5 years?"
    ]

    tech_questions = [
        "Explain Python OOP concepts.",
        "What is a database?",
        "Difference between list and tuple.",
        "What is API?"
    ]

    gd_questions = [
        "Is social media good for students?",
        "Should AI replace human jobs?",
        "Is remote work the future?",
        "Are exams necessary?"
    ]

    if interview_type == "HR Interview":
        return random.choice(hr_questions)
    elif interview_type == "Technical Interview":
        return random.choice(tech_questions)
    else:
        return random.choice(gd_questions)


def analyze_answer(answer):
    if answer.strip() == "":
        return "No answer provided.", 0

    blob = TextBlob(answer)
    sentiment = blob.sentiment.polarity
    grammar_score = len(blob.correct().split())

    score = min(10, max(1, int((grammar_score / 10) + (sentiment * 2) + 5)))

    feedback = f"""
    Sentiment Score: {sentiment}
    Grammar Checked.
    Confidence Level: Moderate
    Suggestions:
    - Try to speak clearly.
    - Improve sentence structure.
    - Add more technical points.
    """

    return feedback, score
