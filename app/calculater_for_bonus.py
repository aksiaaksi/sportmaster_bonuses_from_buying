def calculate_for_bonus(purchase_amount):

    """
    >>> calculate_for_bonus(999)
    0

    >>> calculate_for_bonus(1_000)
    50

    >>> calculate_for_bonus(1668)
    50

    >>> calculate_for_bonus(4995)
    200

    >>> calculate_for_bonus(15199)
    1050

    >>> calculate_for_bonus(49999)
    3430

    >>> calculate_for_bonus(150_000)
    10500

    >>> calculate_for_bonus(169000)
    16900
    """


    share = 1_000
    number_bonus_on_begin_step = 50
    number_bonus_on_medium_step = 70
    number_bonus_on_high_step = 100
    bottom_line = 1_000
    middle_border = 15_000
    upper_bound = 150_000


    if purchase_amount < bottom_line:
        return 0
    if bottom_line <= purchase_amount <= middle_border:
        result = (purchase_amount // share) * number_bonus_on_begin_step
        return result
    if middle_border <= purchase_amount <= upper_bound:
        result1 = ((purchase_amount // share) * number_bonus_on_medium_step)
        return result1
    if  purchase_amount > upper_bound:
        result2 = ((purchase_amount // share) * number_bonus_on_high_step)
        return result2

   # return "Thanks"

#print(calculate_for_bonus(16000))








