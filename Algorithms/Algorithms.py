
def Q_chooses_from_proposed(proposed, preferences):
    choice = None
    for i in range(0, len(preferences)):
        if proposed[preferences[i] - 1]:
            choice = preferences[i]
            break
    return choice


proposed = [True, True, True, False]
preferences = [4, 2, 1, 3]

Q_choice = Q_chooses_from_proposed(proposed, preferences)

print(f"Choice {Q_choice}") # Choice 2

