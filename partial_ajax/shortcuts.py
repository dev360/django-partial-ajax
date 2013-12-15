from django.shortcuts import render as _render

from partial_ajax import THREAD_LOCAL


def render(*args, **kwargs):
    # Set the threading local stuff so we can validate
    # that the user is using this render function if
    # they are using the partials in their templates

    request = args[0]
    partial_name = request.GET.get('partial')
    partial_data = { "name": partial_name } if partial_name  else None
    THREAD_LOCAL.ajax_partial = partial_data if request.is_ajax() else None

    response = _render(*args, **kwargs)
    if THREAD_LOCAL.ajax_partial and 'content' in THREAD_LOCAL.ajax_partial:
        response.content = THREAD_LOCAL.ajax_partial['content']

    return response
