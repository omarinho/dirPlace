from django import template

register = template.Library()

@register.filter
def selected_genre(option):
    GENRES = (
        ('FEM', 'Female'),
        ('MAL', 'Male'),
    )
    return dict(GENRES)[option]

@register.filter
def selected_marital_status(option):
    MARITAL_STATUSES = (
        ('SIN', 'Single'),
        ('MAR', 'Married'),
        ('SEP', 'Separated'),
        ('DIV', 'Divorced'),
        ('WID', 'Widowed'),
        ('COH', 'Cohabiting'),
    )
    return dict(MARITAL_STATUSES)[option]