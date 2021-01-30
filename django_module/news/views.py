from news.form import ItSearchForm, ItRefreshForm
from django.shortcuts import render
from django.views.generic import ListView, FormView
from news.models import ItNews
from django.db.models import Q
import os, sqlite3

class ItNewsView(ListView):
    model = ItNews
    template_name = 'news/news_list.html'
    paginate_by = 10


class ItRefreshFormView(FormView):
    template_name = 'news/itnews_refresh.html'
    form_class = ItRefreshForm
    
    def form_valid(self, form):
        
        if self.request.method == 'POST':
            os.chdir('/Users/jslee/Desktop/my_module_project/django_module')
            con = sqlite3.connect(os.path.abspath('/Users/jslee/Desktop/my_module_project/django_module/db.sqlite3'))
            cur = con.cursor()
            cur.execute('DROP TABLE IF EXISTS news_itnews')
            cur.execute('CREATE TABLE IF NOT EXISTS news_itnews (id INTEGER PRIMARY KEY NOT NULL, title TEXT, writer TEXT, preview TEXT)')
            con.commit()
            os.system('scrapy crawl newsbot')
        
        news_list = ItNews.objects.all()
        upload= {}
        upload['refreshed_list'] = news_list
        
        return render(self.request, self.template_name, upload)

class ItSearchFormView(FormView):
    form_class = ItSearchForm
    template_name = 'news/itnews_search.html'

    def form_valid(self, form):
        schword = self.request.POST['search_word']

        news_list = ItNews.objects.filter(Q(title__icontains=schword)| Q(preview__icontains=schword)|Q(writer__icontains=schword)).distinct()

        # 검색된 결과
        context = {}
        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = news_list


        # request는 사용자가 전달한 정보
        return render(self.request, self.template_name, context)


