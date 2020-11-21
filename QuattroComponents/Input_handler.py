
def user_input(now_turn, guide_msg):
    print(f"[System] {now_turn.user_name}! {guide_msg} : ", end="")
    return __import__('sys').stdin.readline().lower().strip()


def select_number(start, end):
    if end == 6:
        print(f"[System] Select Anonymous player Number({start} ~ {end}) : ", end="")
    else:
        print(f"[System] Select Card Number({start} ~ {end}) : ", end="")

    try:
        num = int(__import__('sys').stdin.readline().strip())
        return num

    except:
        print("[System] Incorrect Number Format!")
        return -1
