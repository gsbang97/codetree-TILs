n = int(input())

B_cards = [int(input()) for _ in range(n)]
A_cards = set(range(1,2*n+1)) - set(B_cards)
A_cards = [True for _ in range(2*n+1)]
A_cards[0] = False
for card in B_cards:
    A_cards[card] = False

score = 0
for card in B_cards:
    is_win = False
    for card in range(card+1,2*n+1):
        if A_cards[card]:
            is_win = True
            A_cards[card] = False
            break
    if is_win:
        score += 1
        continue
    for card in range(card):
        if A_cards[card]:
            A_cards[card] = False
            break
print(score)