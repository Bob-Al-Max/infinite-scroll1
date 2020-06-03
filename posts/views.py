from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Posts
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from posts.forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView





def post_list(request):

    posts = Posts.objects.all()

    return render(request, 'posts/posts.html',{'posts':posts})



class PostListView(ListView):
    paginate_by = 4
    model = Posts
   
    

    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'
    ordering = ['-created_at']




class PostsView(ListView):
    model = Posts
    paginate_by = 4

    context_object_name = 'posts'
    template_name = 'posts/posts-infinite.html'
    ordering = ['-created_at']






   



class PostDetailView(DetailView):
    
    model = Posts
    
    template_name = 'posts/posts_detail.html'
    context_object_name = "hui"

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Posts, id=id_)


class PostCreate(CreateView):
    
    model = Posts
    fields = ['title','slug','content']
    success_url = '/'



class PostUpdate(UpdateView):
    model = Posts
    fields = ['title','content','image']
    template_name_suffix = '_update_form'



class PostDelete(DeleteView):
    model = Posts
    success_url = reverse_lazy('post-list')    
    

          


class ContactView(FormView):
    template_name = 'posts/contact.html'
    form_class = ContactForm
    success_url = '/posts/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)    

   

from django.core.mail import send_mail
from django.conf import settings    
def sen(request):
    subject = 'Сообщение с сайта джанго'
    message = 'Супер! Я смог отправить это сообщение.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['borq_10@mail.ru',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/posts/')



 

    
