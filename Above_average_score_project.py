student_scores = [80, 60, 50, 65, 75, 55]


def sum_score_above_average(p_student_scores):
    score = 0
    number_of_student = 0
    for each_score in p_student_scores:
        score += each_score
        number_of_student += 1
    average_score = score / number_of_student
    above_average_score = 0

    for each_score in p_student_scores:
        if each_score > average_score:
            above_average_score += each_score

    return above_average_score


print(sum_score_above_average(student_scores))
