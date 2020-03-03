from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)

    """
    There are two ways to do this such as;
        => register.filter('cut',cut)
                    or
        => @register.filter(name='cut')
    """
