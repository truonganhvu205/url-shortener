# Clone project
```bash
git init
git clone https://github.com/truonganhvu205/url-shortener-django.git
cd url-shortener-django
```

## Install pipenv
```bash
pip3 install pipenv
```

## Activate virtual environment
```bash
pipenv --python 3.10
pipenv shell
```

## Install Django & frameworks
```bash
# Django
pipenv install django
```

# Run server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Deactivate virtual environment
```bash
exit
```

# Preview project
<table align='center'>
  <tr align='center'>
    <td>Before shorten url</td>
    <td>After shorten url</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/url-shortener-django/blob/main/url-shortener-django/url-shortener-django-pic-1.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/url-shortener-django/blob/main/url-shortener-django/url-shortener-django-pic-2.png' />
    </td>
  </tr>
</table>
