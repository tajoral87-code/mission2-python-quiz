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
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        
        score = 0

        for quiz in self.quizzes:
            quiz.show()

            while True:
                try:
                    user_answer = int(input("정답 번호(1~4): ").strip())

                    if 1 <= user_answer <= 4:
                        break

                    print("1~4 사이의 번호를 입력하세요.")

                except ValueError:
                    print("숫자 1~4를 입력하세요.")

                except (KeyboardInterrupt, EOFError):
                    print("\n퀴즈 풀이를 중단하고 메뉴로 돌아갑니다.")
                    return

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

        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except OSError as error:
            print(f"데이터 저장에 실패했습니다: {error}")

    def load(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, list):
                quiz_data = data
                best_score = 0
            elif isinstance(data, dict):
                quiz_data = data["quizzes"]
                best_score = data.get("best_score", 0)
            else:
                raise ValueError("잘못된 JSON 구조")

            if not isinstance(quiz_data, list):
                raise ValueError("퀴즈 목록이 아닙니다.")

            if type(best_score) is not int or best_score < 0:
                raise ValueError("최고 점수 데이터 오류")

            loaded_quizzes = []

            for item in quiz_data:
                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if not (
                    isinstance(question, str)
                    and question.strip()
                    and isinstance(choices, list)
                    and len(choices) == 4
                    and all(isinstance(c, str) and c.strip() for c in choices)
                    and type(answer) is int
                    and 1 <= answer <= 4
                ):
                    raise ValueError("퀴즈 데이터 오류")

                loaded_quizzes.append(Quiz(question, choices, answer))

            for quiz in loaded_quizzes:
                if not any(
                    existing.question == quiz.question
                    for existing in self.quizzes
                ):
                    self.add_quiz(quiz)

            self.best_score = best_score

        except (OSError, ValueError, TypeError, KeyError, IndexError):
            print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")