from quiz import Quiz
from game import QuizGame

game = QuizGame()

if not game.load():
    game.add_quiz(Quiz(
        "Python에서 출력하는 함수는?",
        ["input", "print", "int", "type"], 2
    ))

    game.add_quiz(Quiz(
        "Python에서 정수로 변환하는 함수는?",
        ["str", "float", "int", "print"], 3
    ))

    game.add_quiz(Quiz(
        "Python에서 문자열을 나타내는 자료형은?",
        ["int", "float", "str", "bool"], 3
    ))

    game.add_quiz(Quiz(
        "Python에서 반복문을 만드는 키워드는?",
        ["if", "for", "def", "return"], 2
    ))

    game.add_quiz(Quiz(
        "Python에서 리스트에 항목을 추가하는 메서드는?",
        ["append", "remove", "sort", "clear"], 1
    ))

while True:
    print("===== Python 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("6. 퀴즈 삭제")
    print("7. 점수 히스토리")

    try:
        menu = int(input("메뉴를 선택하세요: ").strip())

    except ValueError:
        print("숫자 1~7을 입력하세요.")
        continue

    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 게임을 종료합니다.")
        break

    if menu == 1:
        game.play()
    elif menu == 2:
        try:
            # 문제 입력
            while True:
                question = input("문제를 입력하세요: ").strip()
                if question:
                    break
                print("문제는 비워둘 수 없습니다.")

            # 선택지 4개 입력
            choices = []
            for number in range(1, 5):
                while True:
                    choice = input(f"{number}번 선택지: ").strip()
                    if choice:
                        choices.append(choice)
                        break
                    print("선택지는 비워둘 수 없습니다.")

            # 정답 번호 입력
            while True:
                try:
                    answer = int(input("정답 번호(1~4): ").strip())

                    if 1 <= answer <= 4:
                        break

                    print("정답 번호는 1~4여야 합니다.")

                except ValueError:
                    print("정답은 숫자 1~4로 입력하세요.")

            # 힌트 입력 (선택 사항)
            hint = input("힌트를 입력하세요(없으면 Enter): ").strip()

            # 모든 입력이 정상일 때 저장
            game.add_quiz(Quiz(question, choices, answer, hint))
            game.save()
            print("새로운 퀴즈가 등록되었습니다!")

        except (KeyboardInterrupt, EOFError):
            print("\n퀴즈 추가를 취소하고 메뉴로 돌아갑니다.")
    elif menu == 3:
        game.list_quizzes()
    elif menu == 4:
        print(f"역대 최고 점수: {game.best_score}점")
    elif menu == 6:
        game.delete_quiz()
    elif menu == 7:
        game.show_score_history()
    elif menu == 5:
        print("게임을 종료합니다.")
        break
    else:
        print("잘못된 메뉴 번호입니다.")