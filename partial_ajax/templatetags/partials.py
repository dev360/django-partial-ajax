from django.template import Library, Node

from partial_ajax import THREAD_LOCAL


register = Library()


@register.tag('partial')
def ajax_partial(parser, token):
    """
    Partial ajax template
    """
    nodelist = parser.parse(('endpartial'))
    parser.delete_first_token()
    tokens = token.split_contents()
    return PartialNode(nodelist, tokens[1])



class PartialNode(Node):
    """
    PartialNode
    """
    def __init__(self, nodelist, partial_name):
        self.nodelist = nodelist
        self.partial_name = partial_name

    def render(self, context):
        """
        Renders the context
        """
        rendered = self.nodelist.render(context)

        # This is the rendered output of the partial
        # tag.. the simplest thing I can do at this point
        # is to just store this output in the thread local
        # storage for access later
        # Here, we validate the presennce
        if not hasattr(THREAD_LOCAL, 'ajax_partial'):
            raise Exception('To use the {% partial %} template tag you need to use partial_ajax.shortcuts.render when rendering your views.')

        partial_data = THREAD_LOCAL.ajax_partial or {}

        # TLS storage is only updated for the specific partial that
        # is requested
        if self.partial_name == partial_data.get('name'):
            THREAD_LOCAL.ajax_partial['content'] = rendered

        return rendered


