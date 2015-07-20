from django import template

register = template.Library()


#inspired by
# http://timonweb.com/posts/creating-custom-template-filter-that-injects-adsense-ad-code-after-n-paragraph-in-django/

@register.filter
def paragraph(value, arg):
    """Selects the first arg paragraphs from an html text"""
    # Break down content into paragraphs
    paragraphs = value.split('</p>')
    # Check if paragraph we want to post after exists
    if arg < len(paragraphs):
        value = '</p>'.join(paragraphs[0:arg]) + '</p>'
    return value


@register.filter
def get_color(article):
    """Returns the class of a background color, based on the id of a post"""
    # List of classes with different background colors
    colors = ['back-orange', 'back-green', 'back-grey', 'back-blue', ]  # 'back-violet', 'back-red', ]

    # Attribute a color based on the id of the article
    color = article % len(colors)

    return colors[color]

