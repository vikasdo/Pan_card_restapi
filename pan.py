from random import randrange


class BackendError(Exception):
    pass


def get_pan_data(pan_number):
    num = randrange(10)


    if num in (8,9):
        raise BackendError
    
    return {
        'pan': pan_number,
        'name': 'Dinesh Kumar',
        'dob': '25-10-1990',
        'father_name': 'Hari Kumar'
    }