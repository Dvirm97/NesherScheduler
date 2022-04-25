import backtracker
import random

random.sample(range(1, 100), 3)  # [77, 52, 45]


def validate(soldiers, num_of_shifts):
    availability = {}
    for soldier in soldiers:
        availability[soldier['id']] = list(filter(lambda shift_id: shift_id not in soldier['constraints'],
                                                  range(1, num_of_shifts + 1)))

    def validate_schedule(schedule, up_to_shift):
        soldiers_occupied = []
        for shift in schedule:
            if shift['shift_id'] <= up_to_shift + 1:

                if shift['shift_id'] not in availability[shift['soldier_id']]:
                    return False

                soldiers_occupied.append(shift['soldier_id'])

        if len(soldiers_occupied) != len(set(soldiers_occupied)):
            return False

        return True

    solution = backtracker.solve(availability, validate_schedule, num_of_shifts)

    if solution:
        return availability
    else:
        return None
