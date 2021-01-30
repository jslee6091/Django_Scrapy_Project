from django.shortcuts import render
from django.views.generic import ListView, FormView
from world_news.models import WorldNews
from world_news.form import WorldSearchForm, WorldRefreshForm
from django.db.models import Q
import os, sqlite3

# Create your views here.
class WorldNewsView(ListView):
    model = WorldNews
    template_name = 'world_news/world_list.html'
    paginate_by = 10


class WorldRefreshFormView(FormView):
    template_name = 'world_news/world_refresh.html'
    form_class = WorldRefreshForm
    
    def form_valid(self, form):
        
        if self.request.method == 'POST':
            os.chdir('/Users/jslee/Desktop/my_module_project/django_module')
            con = sqlite3.connect(os.path.abspath('/Users/jslee/Desktop/my_module_project/django_module/db.sqlite3'))
            cur = con.cursor()
            cur.execute('DROP TABLE IF EXISTS world_news')
            cur.execute('CREATE TABLE IF NOT EXISTS world_news (id INTEGER PRIMARY KEY NOT NULL, title TEXT, writer TEXT, preview TEXT)')
            con.commit()
            os.system('scrapy crawl newsbot3')
        
        news_list = WorldNews.objects.all()
        upload= {}
        upload['refreshed_list'] = news_list
        
        return render(self.request, self.template_name, upload)


class WorldSearchFormView(FormView):
    form_class = WorldSearchForm
    template_name = 'world_news/world_search.html'

    def form_valid(self, form):
        schword = self.request.POST['search_word']

        news_list = WorldNews.objects.filter(Q(title__icontains=schword)| Q(preview__icontains=schword)|Q(writer__icontains=schword)).distinct()

        # 검색된 결과
        context = {}
        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = news_list


        # request는 사용자가 전달한 정보
        return render(self.request, self.template_name, context)
