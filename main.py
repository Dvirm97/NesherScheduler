from hungarian_algorithm import algorithm
from data import soldiers, shifts


def schedule_soldiers(soldiers_available_shifts):
    soldiers_preferences = calculate_preferences(soldiers_available_shifts)
    return algorithm.find_matching(soldiers_preferences, 'max', return_type = 'list')


def calculate_preferences(soldiers_available_shifts):
    soldiers_preferences = {}
    for soldier_id, available_shifts in soldiers_available_shifts.items():
        soldier = get_soldier_by_id(soldier_id)
        type_preference = soldier.get('type_preference')
        location_preference = soldier.get('location_preference')
        preferences_dict = {}

        for shift_id in available_shifts:
            shift_grade = 0
            shift_info = get_shift_by_id(shift_id)
            if shift_info.get('type') == type_preference:
                shift_grade += 1
            if shift_info.get('location') == location_preference:
                shift_grade += 1
            preferences_dict[str(shift_id)] = shift_grade
        
        soldiers_preferences[str(soldier_id)] = preferences_dict
    return soldiers_preferences


def get_shift_by_id(shift_id):
    for shift in shifts:
        if shift.get('id') == shift_id:
            return shift


def get_soldier_by_id(soldier_id):
    for soldier in soldiers:
        if soldier.get('id') == soldier_id:
            return soldier


def main():
    soldiers_available_shifts = {'8686518': [1, 2, 3],
                                 '8463627': [2, 3, 4, 5],
                                 '8811066': [1, 2, 3, 4, 5],
                                 '6631368': [4],
                                 '9035532': [2, 3, 4]}
    schedule = schedule_soldiers(soldiers_available_shifts)
    print(schedule)


if __name__ == '__main__':
    main()
