from django.shortcuts import render, HttpResponse
import bitly_api 

# Create your views here.

def url_shortner(requests):
    response = render(requests, 'url_shortner.html')
    if requests.method == 'POST':
        print('Request meethod is post')
        url = requests.POST.get('url')
        print(url)
        BITLY_ACCESS_TOKEN ="895a6e34f3846e6bbc446da04dae96caa64ec72c"
        access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
        full_link = url
        short_url = access.shorten(full_link) 
        print('Short URL = ',short_url['url'])
        response = render(requests, 'url_shortner.html',{'short_url':short_url['url']})

    return response





