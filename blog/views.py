from django.shortcuts import render
from aakaar_admin.models import Blog,BlogDetails

def blog_view(request):
    try:
        blogs = Blog.objects.all()
        blogcontent = BlogDetails.objects.all().last()
    except Exception as e:
        blogs = None
        blogcontent = None
        print('Exception in about_us in index_view(): ', e)

    context = { 
        'Blogs':blogs,
        'blogcontent':blogcontent,
    }
    return render(request, 'blog/blog.html', context)


def Blog_details(request,blog_id):
    try:
        Blog_details = Blog.objects.get(id=blog_id)
        ids = [blog_id-1,blog_id+1]
        blogs = Blog.objects.filter(id__in=ids)
    except Exception as e:
        Blog_details = None
        blogs = None
        
    context = {"BlogDetails":Blog_details,"blogs":blogs}
    return render(request,'blog/blog_details.html',context)