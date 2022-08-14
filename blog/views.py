from django.shortcuts import render

def blog_view(request):
    context = {}
    return render(request, 'blog/blog.html', context)