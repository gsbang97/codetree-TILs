n = int(input())

B_cards = [int(input()) for _ in range(n)]
A_cards = set(range(1,2*n+1)) - set(B_cards)

score = 0
for card in B_cards:
    is_win = False
    for card in range(card+1,2*n+1):
        if card in A_cards:
            is_win = True
            A_cards.remove(card)
            break
    if is_win:
        score += 1
        continue
    for card in range(card):
        if card in A_cards:
            A_cards.remove(card)
            break
print(score)