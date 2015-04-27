from django.shortcuts import render


def graph_test(request):
    return render(request,
                  'graphs/graph_test.html',
                  {'context': 'context',
                   'numbers': [1, 2, 3, 20]})
