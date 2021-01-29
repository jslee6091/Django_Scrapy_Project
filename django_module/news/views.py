from news.form import ItDataSearchForm
from django.shortcuts import render
from django.views.generic import ListView, FormView
from news.models import ItNews
from django.db.models import Q

class ItNewsView(ListView):
    model = ItNews
    template_name = 'news/news_list.html'
    paginate_by = 10

class ItDataSearchFormView(FormView):
    form_class = ItDataSearchForm
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


