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
        print("퀴즈 추가 기능은 준비 중입니다.")
    elif menu == 3:
        game.list_quizzes()
    elif menu == 4:
        print("점수 확인을 선택했습니다.")
    elif menu == 5:
        print("게임을 종료합니다.")
        break
    else:
        print("잘못된 메뉴 번호입니다.")