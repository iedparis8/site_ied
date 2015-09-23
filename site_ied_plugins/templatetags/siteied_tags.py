from django import template

register = template.Library()


#inspired by
# http://timonweb.com/posts/creating-custom-template-filter-that-injects-adsense-ad-code-after-n-paragraph-in-django/

@register.filter
def paragraph(value, arg):
    """Selects the first arg paragraphs from an html text"""
    # Break down content into paragraphs
    paragraphs = value.split('</')
    # Check if paragraph we want to post after exists
    if arg < len(paragraphs):
        tag = paragraphs[arg].split('>', 1)
        value = '</'.join(paragraphs[0:arg]) + '</' + tag[0] + '><p>...</p>'
        print value
    return value


@register.filter
def get_color(article):
    """Returns the class of a background color, based on the id of a post"""
    # List of classes with different background colors
    colors = ['orange', 'green', 'grey', 'blue', ]  # 'violet', 'red', ]

    # Attribute a color based on the id of the article
    color = int(article) % len(colors)

    return colors[color]

