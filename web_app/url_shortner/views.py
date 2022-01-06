from django.shortcuts import render, HttpResponse
import bitly_api 
from simplecrypt import encrypt, decrypt
import codecs

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


def pastelockly(requests):
    response = render(requests, 'pastelockly.html')
    if requests.method == 'POST':
        print('pastelocky post methos')
        text = requests.POST.get('textt')
        secret_key = requests.POST.get('secret_key')
        cipher_text = encrypt(secret_key, text)
        print(text,secret_key)
        print('cipher_text',str(cipher_text))
        print('cipher_text',type(cipher_text))
        # print('decryped',decrypt(secret_key, cipher_text))
    return response

def viewsecrettext(requests):
    response = render(requests, 'viewsecrettext.html')
    if requests.method == 'POST':
        secret_key = requests.POST.get('secret_key')
        cipher_text = requests.POST.get('cipher_text')
        cipher_text = cipher_text[2:-2]
        cipher_text_bytes = cipher_text.encode()
        print('cipher_text',cipher_text,'secret_key', secret_key)
        print('cipher_text_bytes',cipher_text_bytes)
        print('decrypted msg',decrypt(secret_key, cipher_text_bytes))
    return response