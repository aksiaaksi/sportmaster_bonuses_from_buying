def calculate_for_bonus(purchase_amount, amount_previous_purchases):

    """
    >>> calculate_for_bonus(999,0)
    0

    >>> calculate_for_bonus(1_000, 1_100)
    50

    >>> calculate_for_bonus(1_668, 2_000)
    50

    >>> calculate_for_bonus(4_995, 15_000)
    200

    >>> calculate_for_bonus(15199, 15_001)
    1050

    >>> calculate_for_bonus(49999, 150_001)
    4900

    >>> calculate_for_bonus(150_000, 10)
    7500

    >>> calculate_for_bonus(169_000, 160_000)
    16900
    """


    share = 1_000
    number_bonus_on_begin_step = 50
    number_bonus_on_medium_step = 70
    number_bonus_on_high_step = 100
    bottom_line = 0
    bottom_line_min = 1000
    middle_border = 15_000
    upper_bound = 150_000


    if bottom_line < purchase_amount <  bottom_line_min:
        return 0

    if bottom_line <= amount_previous_purchases <= middle_border:
        result = (purchase_amount // share) * number_bonus_on_begin_step
        return result
    if middle_border <= amount_previous_purchases <= upper_bound:
        result = ((purchase_amount // share) * number_bonus_on_medium_step)
        return result
    if  amount_previous_purchases > upper_bound:
        result = ((purchase_amount // share) * number_bonus_on_high_step)
        return result

    #return

print(calculate_for_bonus(169_000, 160_000))








