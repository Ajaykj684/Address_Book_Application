#utility functions for validation using pydantic.

def validate_location(cls, value):
    if not (-90 <= value <= 90):
        raise ValueError('Invalid latitude or longitude value')
    return value

def name_must_not_be_empty(cls, value):
    if not value:
        raise ValueError('Name must not be empty')
    return value

def street_must_not_be_empty(cls, value):
    if not value:
        raise ValueError('Street must not be empty')
    return value

def city_must_not_be_empty(cls, value):
    if not value:
        raise ValueError('City must not be empty')
    return value

def state_must_not_be_empty(cls, value):
    if not value:
        raise ValueError('State must not be empty')
    return value

def country_must_not_be_empty(cls, value):
    if not value:
        raise ValueError('Country must not be empty')
    return value

def zip_must_not_be_empty(cls, value):
    if not value:
        raise ValueError('Zip must not be empty')
    return value