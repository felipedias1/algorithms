def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for person in permanence_period:
            if person[0] <= target_time <= person[1]:
                count += 1
        return count
    except (ValueError, TypeError):
        return None
