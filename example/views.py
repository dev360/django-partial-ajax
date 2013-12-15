from partial_ajax.shortcuts import render


def index(request):
    """
    Example page
    """
    contacts = [
        { "first_name": "Christian", "last_name": "Toivola"},
        { "first_name": "Orlando", "last_name": "Garcia"},
        { "first_name": "Larry", "last_name": "Garcia"},
        { "first_name": "Brian", "last_name": "Dosal"},
        { "first_name": "Eric", "last_name": "Dosal"},
        { "first_name": "David", "last_name": "Small"},
        { "first_name": "Steven", "last_name": "Restrepo"},
    ]

    sort_attr = request.GET.get('sort_attr', 'first_name')
    sort_dir = request.GET.get('sort_dir', 'asc')

    contacts = sorted(contacts, key=lambda x: x.get(sort_attr))
    if sort_dir == 'desc':
        contacts.reverse()

    context = dict(
        contacts = contacts,
        sort_attr = sort_attr,
        sort_dir = sort_dir,
    )
    return render(request, 'index.html', context)

