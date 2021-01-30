from economic_news.form import RefreshForm, SearchForm
from django.shortcuts import render
from django.views.generic import ListView, FormView
from economic_news.models import EconomicNews
from django.db.models import Q
import os, sqlite3


# Create your views here.
class EconomicNewsView(ListView):
    model = EconomicNews
    template_name = 'economic_news/economic_list.html'

    paginate_by = 10


class RefreshFormView(FormView):
    template_name = 'economic_news/economic_refresh.html'
    form_class = RefreshForm
    
    def form_valid(self, form):
        
        if self.request.method == 'POST':
            os.chdir('/Users/jslee/Desktop/my_module_project/django_module')
            con = sqlite3.connect(os.path.abspath('/Users/jslee/Desktop/my_module_project/django_module/db.sqlite3'))
            cur = con.cursor()
            cur.execute('DROP TABLE IF EXISTS economic_news')
            cur.execute('CREATE TABLE IF NOT EXISTS economic_news (id INTEGER PRIMARY KEY NOT NULL, title TEXT, writer TEXT, preview TEXT)')
            con.commit()
            os.system('scrapy crawl newsbot2')
        
        news_list = EconomicNews.objects.all()
        upload= {}
        upload['refreshed_list'] = news_list
        
        return render(self.request, self.template_name, upload)

class SearchFormView(FormView):
    form_class = SearchForm
    template_name = "economic_news/economic_search.html"
    
    # 검색 할때의 페이지와 검색 결과가 나오는 페이지를 같게 한다.
    def form_valid(self, form):
        schword = self.request.POST['search_word']

        news_list = EconomicNews.objects.filter(Q(title__icontains=schword)| Q(preview__icontains=schword)|Q(writer__icontains=schword)).distinct()

        # 검색된 결과
        context = {}
        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = news_list


        # request는 사용자가 전달한 정보
        return render(self.request, self.template_name, context)
