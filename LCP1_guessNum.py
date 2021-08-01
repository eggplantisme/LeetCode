class Solution:
    def game(self, guess, answer):
        right = 0
        for i in range(3):
            if guess[i] == answer[i]:
                right += 1
        return right