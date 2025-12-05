class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = 0
        score2 = 0
        for i in range(1, len(player1)):
            if player1[i-1] == 10 or (player1[i-2] == 10 and i >= 2):
                score1 += 2 * player1[i]
                print(score1)
            else:
                score1 += player1[i]
                print(score1)
            if player2[i-1] == 10 or (player2[i-2] == 10 and i >= 2):
                score2 += 2 * player2[i]
                print(score2)
            else:
                score2 += player2[i]
                print(score2)
        score1 += player1[0]
        score2 += player2[0]
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0
            
            