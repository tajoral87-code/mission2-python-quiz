import json
import random
from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.score_history = []

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def show_score_history(self):
        if not self.score_history:
            print("아직 점수 기록이 없습니다.")
            return

        print("===== 점수 히스토리 =====")

        for number, record in enumerate(self.score_history, start=1):
            print(
                f"{number}회차: "
                f"{record['total']}문제 중 "
                f"{record['correct']}개 정답 / "
                f"{record['score']}점"
            )

    def delete_quiz(self):
        if not self.quizzes:
            print("삭제할 퀴즈가 없습니다.")
            return
        self.list_quizzes()

        try:
            number = int(input("삭제할 문제 번호: ")) 
        except ValueError:
            print("숫자를 입력하세요.")
            return
        except (KeyboardInterrupt, EOFError):
            print("\n삭제를 취소했습니다.")
            return

        if not 1 <= number <= len(self.quizzes):
            print("존재하지 않는 문제 번호입니다.")
            return
            
        deleted_quiz = self.quizzes.pop(number - 1)
        self.save()
        print(f"'{deleted_quiz.question}' 문제가 삭제되었습니다.")

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        
        
        
        score = 0
        correct_count = 0

        print(f"현재 등록된 문제: {len(self.quizzes)}개")
        while True:
            try:
                question_count = int(input(f"몇 문제를 풀겠습니까? (1~{len(self.quizzes)}): "))
            
                if 1 <= question_count <= len(self.quizzes):
                    break 

                print(f"1~{len(self.quizzes)} 사이의 숫자를 입력하세요.") 

            except ValueError:
                print("숫자를 입력하세요.")  

            except (KeyboardInterrupt, EOFError):
                print("\n문제 수 선택을 중단하고 메뉴로 돌아갑니다.")
                return      

        quiz_list = self.quizzes.copy()
        random.shuffle(quiz_list)
        quiz_list = quiz_list[:question_count]
        
        for quiz in quiz_list:
            quiz.show()

            hint_used = False

            if quiz.hint:
                print("이 문제에는 힌트가 있습니다.")

                while True:
                    try:
                        hint_choice = input("힌트를 보시겠습니까? (y/n): ").strip().lower()

                        if hint_choice in ("y", "n"):
                            break

                        print("y 또는 n을 입력하세요.")

                    except (KeyboardInterrupt, EOFError):
                        print("\n퀴즈 풀이를 중단하고 메뉴로 돌아갑니다.")
                        return    

                if hint_choice == "y":
                    print(f"힌트: {quiz.hint}")
                    hint_used = True

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
                correct_count += 1
                score += 1 if hint_used else 2
            else:
                print("오답입니다.")

        print(f"정답 개수: {correct_count}/{len(quiz_list)}")
        print(f"최종 점수: {score}/{len(quiz_list) * 2}")

        self.score_history.append({
            "total": len(quiz_list),
            "correct": correct_count,
            "score": score
        })

        if correct_count > self.best_score:
            self.best_score = correct_count
            print("새로운 최고 점수입니다!")

        self.save()

    def save(self):
        data = {
            "best_score": self.best_score,
            "score_history": self.score_history,
            "quizzes": []
        }

        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer,
                "hint": quiz.hint 
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
                score_history = []
            elif isinstance(data, dict):
                quiz_data = data["quizzes"]
                best_score = data.get("best_score", 0)
                score_history = data.get("score_history", [])
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
                hint = item.get("hint", "")

                if not (
                    isinstance(question, str)
                    and question.strip()
                    and isinstance(choices, list)
                    and len(choices) == 4
                    and all(isinstance(c, str) and c.strip() for c in choices)
                    and type(answer) is int
                    and 1 <= answer <= 4
                    and isinstance(hint, str)
                ):
                    raise ValueError("퀴즈 데이터 오류")
              
                loaded_quizzes.append(Quiz(question, choices, answer, hint))

            for quiz in loaded_quizzes:
                if not any(
                    existing.question == quiz.question
                    for existing in self.quizzes
                ):
                    self.add_quiz(quiz)

            if not isinstance(score_history, list):
                raise ValueError("점수 기록 데이터 오류")

            for record in score_history:
                if not (
                    isinstance(record, dict)
                    and type(record.get("total")) is int
                    and type(record.get("correct")) is int
                    and type(record.get("score")) is int
                    and record["total"] >= 1
                    and 0 <= record["correct"] <= record["total"]
                    and 0 <= record["score"] <= record["total"] * 2
                ):
                    raise ValueError("점수 기록 항목 오류")

            self.best_score = best_score
            self.score_history = score_history
            return True

        except (OSError, ValueError, TypeError, KeyError, IndexError):
            print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
            return False