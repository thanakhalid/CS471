from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Comments, Poems

# Create your views here.
def show_base(request):
    return render(request, 'base.html')
def home(request):
    return render(request,'home.html',{})
def signUp(request):
    return render(request,'Registration.html')
def signIn(request):
    return render(request,'Login.html')
def cpoems(request):
    return render(request,'cpoems.html')
def poems(request, poet_cat):
    poems = Poems.objects.filter(poet_cat=poet_cat)
    context = {'poems': poems}
    return render(request, 'poems.html', context)
def poem(request, poem_id):
    poem = get_object_or_404(Poems, pk=poem_id)
    context = {'poem': poem}
    return render(request, 'poem.html', context)
def add_comment(request, poem_id):
    if request.method == 'POST':
        poem = get_object_or_404(Poems, pk=poem_id)
        text = request.POST.get('text')
        if text:
            comment = Comments.objects.create(poem=poem, user=request.user, text=text)
            comment.save()
    return redirect('poem', poem_id=poem_id)