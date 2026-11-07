from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = []

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def list_quizzes(self):
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def play(self):
        score = 0

        for quiz in self.quizzes:
            quiz.show()

            try:
                user_answer = int(input("정답 번호(1~4): ").strip())
            except ValueError:
                print("숫자를 입력해야 합니다.")
                continue

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print("오답입니다.")

        print(f"최종 점수: {score}/{len(self.quizzes)}")