import json
from question import Question


def load_questions(filename):
    """ Загрузка вопроса """
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
    # При старте программы вопросы считываются и раскладываются в экземпляры класса Question
    # Все экземпляры складываются в список questions
    questions = []
    for i in data:
        text = i['q']
        difficulty = int(i['d'])
        right_answer = i['a']
        # Создание экземпляров класса Question
        question = Question(text, difficulty, right_answer)
        questions.append(question)
    return questions


def build_statistics(questions):
    """ Загрузка результатов """
    score = 0
    count = 0
    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count + 1

    return f'Вот и всё!\n' \
           f'Отвечено {count} вопроса из 10\n' \
           f'Набрано баллов: {score}'
