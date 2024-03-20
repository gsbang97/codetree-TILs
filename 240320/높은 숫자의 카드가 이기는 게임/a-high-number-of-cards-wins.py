n = int(input())

B_cards = [int(input()) for _ in range(n)]
A_cards = set(range(1,2*n+1)) - set(B_cards)
A_cards = [True for _ in range(2*n+1)]
A_cards[0] = False
for card in B_cards:
    A_cards[card] = False

score = 0
min_card = 0
for card in B_cards:
    is_win = False
    for win_card in range(card+1,2*n+1):
        if A_cards[win_card]:
            is_win = True
            A_cards[win_card] = False
            break
    if is_win:
        score += 1
        continue
    for lose_card in range(min_card,card):
        if A_cards[lose_card]:
            min_card = lose_card
            A_cards[lose_card] = False
            break
print(score)