voters = ["A", "B", "C"]
votes = {"A": 0, "B": 0, "C": 0}
n = int(input("Enter number of voters: "))
for i in range(n):
    vote = input("Vote (A/B/C): ").upper()
    if vote in votes:
        votes[vote] += 1
    else:
        print("Invalid vote")
print("Results:", votes)
winner = max(votes, key=votes.get)
print("Winner is:", winner)

'''Output
Enter number of voters: 5
Vote (A/B/C): a
Vote (A/B/C): a
Vote (A/B/C): b
Vote (A/B/C): a
Vote (A/B/C): c
Results: {'A': 3, 'B': 1, 'C': 1}
Winner is: A
'''
