from economic_news.form import DataForm, DataSearchForm
from django.shortcuts import render
from django.views.generic import ListView, FormView
from economic_news.models import EconomicNews
from django.db.models import Q
import os


# Create your views here.
class EconomicNewsView(ListView):
    model = EconomicNews
    template_name = 'economic_news/economic_list.html'

    paginate_by = 10


class DataFormView(FormView):
    template_name = 'economic_news/economic_list.html'
    form_class = DataForm
    success_url = 'economicnews/'
    context_object_name = 'eco'

    def form_valid(self, form):
        print('this request', self.request)
        
        os.chdir('/Users/jslee/Desktop/my_module_project/django_module')
        os.system('scrapy crawl newsbot2')
        
        return super().form_valid(form)

class DataSearchFormView(FormView):
    form_class = DataSearchForm # form.py에 생성
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
