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
        print("퀴즈 풀기를 선택했습니다.")
    elif menu == 2:
        print("퀴즈 추가를 선택했습니다.")
    elif menu == 3:
        print("퀴즈 목록을 선택했습니다.")
    elif menu == 4:
        print("점수 확인을 선택했습니다.")
    elif menu == 5:
        print("게임을 종료합니다.")
        break
    else:
        print("잘못된 메뉴 번호입니다.")