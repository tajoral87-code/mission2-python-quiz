import json
from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

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
        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
            self.save()

    def save(self):
        data = {
            "best_score": self.best_score,
            "quizzes": []
        }

        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })

        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, list):
                quiz_data = data
            else:
                quiz_data = data["quizzes"]
                self.best_score = data.get("best_score", 0)

            for item in quiz_data:
                quiz = Quiz(
                    item["question"],
                    item["choices"],
                    item["answer"]
                )

                if not any(
                    existing.question == quiz.question
                    for existing in self.quizzes
                ):
                    self.add_quiz(quiz)

        except (FileNotFoundError, json.JSONDecodeError, TypeError, KeyError):
            print("저장된 퀴즈를 불러올 수 없습니다.")