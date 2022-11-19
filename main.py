import random
from utils import load_questions, build_statistics

# основная логика программы
if __name__ == '__main__':
    filename = 'questions.json'
    # загрузка вопроса через функцию для загрузки вопроса
    questions = load_questions(filename)
    # перемешивание вопросов
    random.shuffle(questions)

    for question in questions:
        # задаем вопрос и считываем ответ
        print(question.build_question())
        user_answer = input("Введите ваш ответ: ")
        question.user_answer = user_answer
        # выводим статистику
        print(question.build_feedback())

    print(build_statistics(questions))
