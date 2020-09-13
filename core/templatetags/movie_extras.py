from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString

register=Library()

@register.simple_tag
def movie_format(movie,short=False):
    if short:
        return f'{movie.title} ({movie.released.year})'
    return f'{movie.title}({movie.released.year})-{movie.genre}'

@register.filter
def att_as_f(obj,attrname):
    label=escape(attrname.capitalize())
    value=escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value}</p>')