from django.shortcuts import render, redirect
from .models import ShortenedURL
from .forms import ShortenURLForm
import string, random

# Create your views here.
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(request):
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_code = generate_short_code()
            
            shortened_url = ShortenedURL(
                original_url=original_url,
                short_code=short_code
            )
            shortened_url.save()
            
            return render(request, 'success.html', {'shortened_url': shortened_url})
    else:
        
        form = ShortenURLForm()
        
    return render(request, 'shorten_url.html', {'form': form})

def redirect_to_original(request, short_code):
    try:
        shortened_url = ShortenedURL.objects.get(short_code=short_code)
        
        return redirect(shortened_url.original_url)
    
    except ShortenedURL.DoesNotExist:
        return render(request, 'not_found.html')