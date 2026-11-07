from quiz import Quiz
from game import QuizGame

game = QuizGame()

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

    try:
        menu = int(input("메뉴를 선택하세요: ").strip())
    except ValueError:
        print("숫자 1~5를 입력하세요.")
        continue

    if menu == 1:
        game.play()
    elif menu == 2:
        question = input("문제를 입력하세요: ").strip()

        choices = []
        for number in range(1, 5):
            choice = input(f"{number}번 선택지: ").strip()
            choices.append(choice)

        try:
            answer = int(input("정답 번호(1~4): ").strip())
        except ValueError:
            print("정답은 숫자로 입력해야 합니다.")
            continue

        if not question or any(not choice for choice in choices):
            print("문제와 선택지는 비워둘 수 없습니다.")
        elif answer not in range(1, 5):
            print("정답 번호는 1~4여야 합니다.")
        else:
            game.add_quiz(Quiz(question, choices, answer))
            print("새로운 퀴즈가 등록되었습니다!")
    elif menu == 3:
        game.list_quizzes()
    elif menu == 4:
        print("점수 확인을 선택했습니다.")
    elif menu == 5:
        print("게임을 종료합니다.")
        break
    else:
        print("잘못된 메뉴 번호입니다.")