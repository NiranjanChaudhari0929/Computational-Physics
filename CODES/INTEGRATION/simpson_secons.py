
def funct():


def simpson_three_by_eight(lower_limit, upper_limit, interval_limit):
    interval_size = (float(upper_limit - lower_limit) / interval_limit)
    sum = funct(lower_limit) + funct(upper_limit)
    for i in range(1, interval_limit):
        if (i % 3 == 0):
            sum = sum + 2 * funct(lower_limit + i * interval_size)
        else:
            sum = sum + 3 * funct(lower_limit + i * interval_size)

    print((float(3 * interval_size) / 8) * sum)