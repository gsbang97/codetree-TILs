n = int(input())

B_cards = [int(input()) for _ in range(n)]
A_cards = list(set(range(1,2*n+1)) - set(B_cards))
A_cards.sort()
B_cards.sort()

B_idx = 0
score = 0
for A_idx in range(n):
    if B_idx < n and A_cards[A_idx] > B_cards[B_idx]:
        score += 1
        B_idx += 1

print(score)