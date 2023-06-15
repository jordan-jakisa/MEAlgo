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
print(f"Choice {Q_choice}")  # Choice 2


def generate_true_false_list(number):
    true_false_list = []
    for i in range(0, number + 1):
        true_false_list.append(i % 2 == 0)
    return true_false_list


def Q_collects_proporsals(K, Q_order):
    proposed = [False] * len(K)
    for i in range(0, len(K)):
        if K[i] != None:
            if K[i][0] == Q_order:
                proposed[i] = True
    return proposed


"""
Unit test
For simplicity, every king(k) has the same preference except k2
In the first round K_2 will not propose to Queen Q4 but Q2
"""

K1_preferences = [4, 2, 1, 3]
K2_preferences = [4, 2, 1, 3]
K3_preferences = [3, 4, 1, 2]
K4_preferences = [4, 2, 1, 3]

Q_order = 4  # 2

proposed = ["False", "False", "False", "False"]
proposed = Q_collects_proporsals([K1_preferences, K2_preferences, K3_preferences, K4_preferences], Q_order)

print(f"Q_{Q_order} received proposals : {proposed}")
