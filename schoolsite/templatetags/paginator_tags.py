from django import template


register = template.Library()

@register.simple_tag
def replace_url(request, field, value):
	d = request.GET.copy()
	d[field] = value

	return d.urlencode()
