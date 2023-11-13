def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for period in permanence_period:
        start, end = period
        # isinstance valida os tipos do dado, passando o item e o que ele é
        if None in period or isinstance(start, str) or isinstance(end, str):
            return None
        if target_time >= start and target_time <= end:
            count += 1
    return count
