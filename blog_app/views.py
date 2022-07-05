from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PostCreateForm
from .models import Post

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        context = {
            'posts':post               ## lo mandamos al a html
        }
        return render(request,"blog_list.html",context)

class  BlogCreateView(View):
    ## definimos método get
    def get(self,request, *args, **kwargs):
        form = PostCreateForm()     ##   Pedimos el formulario
        
        context = {
            'form':form
        }
        return render(request,'blog_create.html', context)

    ## definimos método post
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostCreateForm(request.POST)   # si el método es post, vamos a pedir el formulario para
                                        ## para pasarle información que viene por el post
            if form.is_valid(): ## si el formulario es valido, queremos obtener la información de nuestro formulario
                title = form.cleaned_data.get('title')  ## del form estamos obteniendo los datos, en este caso el de title
                content = form.cleaned_data.get('content')  ## recordemos que estos campos los declaramos en el formulario

                p, created = Post.objects.get_or_create(title=title, content=content) ## ya que obtuvimos los campos, creamos el post
                                ## este Post, hace referencia al modelo llamado Post, por ello fue que lo importamos
                p.save()  ## guardamos los datos en el modelo
                return redirect('blog:home')

        context = {}
        return render(request, 'blog_create.html',context)


## ahora, queremos ver los posts específicos  
class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)   ## estamos obteniendo el post  de la base de datos 
        context = {
            'post':post
        }
        return render(request, 'blog_detail.html', context)

class BlogUpdateView(UpdateView):
    ## al  updateview le debemos pasar que modelo deseamos editar 
    model = Post
    ## luego le pasamos los campos que deseamos editar 
    fields = ['title', 'content']
    ## luego pasamos la vista que vamos a usar para actualizar que es similar a la de crear 
    template_name = 'blog_update.html'

        ## el siguiente método es para que nos rediriga a home después de haber hecho el update 
    def get_success_url(self): 
        pk = self.kwargs['pk'] ## esto hace referencia a la información del objeto que estamos llamando, en este caso self 
        return reverse_lazy('blog:details', kwargs={'pk':pk})

class BlogDeleteView(DeleteView):
    ## llamamos al modelo que deseamos eliminar 
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:home')


