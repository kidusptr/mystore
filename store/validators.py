from django.core.exceptions import ValidationError


def validate_file_size(value):
    max_size_in_kb = 100
    if value.size > max_size_in_kb * 1024:
        raise ValidationError("File size should be less than 100KB")
