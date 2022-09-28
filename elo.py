# dif: the difference between the rankings of two animes
# returns the largest possible k-value to be used in the elo calculation
# k-value is based off the difference in score between two animes
# if the animes are close in ranking, then the k-value is smaller
# and vise verse
def kvalue(dif):
    if 100 >= dif > 50:
        return (15, 15)
    elif 200 >= dif > 100:
        return (25, 20)
    elif 500 >= dif > 200:
        return (30, 15)
    elif dif > 500:
        return (35, 10)
    else:
        return (10, 10)

# elo: calculates the elo scores for each anime based off the user choice
# rating_a : the current elo score of anime A
# rating_b : the current elo score of anime B
# score_a : the match score for anime A (0 for loss, 1 for win)
# returns: the updated elo scores for anime A and B
def elo_rating(rating_a, rating_b, score_a):
    highk, lowk = kvalue(abs(rating_a - rating_b))
    if (rating_a > rating_b and score_a) or (rating_b > rating_a and not score_a):
        k_value = lowk
    else:
        k_value = highk

    if score_a:
        score_b = 0
    else:
        score_b = 1

    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    expected_b = 1 / (1 + 10 ** ((rating_a - rating_b) / 400))
    elo_a = round(rating_a + k_value * (score_a - expected_a), 2)
    elo_b = round(rating_b + k_value * (score_b - expected_b), 2)
    return elo_a, elo_b
