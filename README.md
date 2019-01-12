# Django-Web-Crawler
Django app which can be used to crawl a website

# Steps to run the project
1. Install the requirements by running `pip3 install -r requirements.txt`
2. Run the project by exexcuting `python manage.py runserver 0.0.0.0:8000`
3. Access the project at [http://0.0.0.0:8000/](http://0.0.0.0:8000/)
4. Enter a URL in the input field and wait for the results
5. To use it as a REST API, keep the server running and frame the URL as `http://0.0.0.0:8000/api/?url=URL_TO_BE_CRAWLED`. Example: `http://0.0.0.0:8000/api/?url=google.com`