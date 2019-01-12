from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .crawler import Crawler


# To prevent CSRF token issues
@csrf_exempt
def urlInput(request):
    # import pudb; pudb.set_trace();
    try:
        url = request.GET['url']
        crawledData = Crawler(url, 25)
        crawled_urls = clean_output(crawledData.crawled_urls)
        response = ":::::::::::::::::::::::" + "URL COUNT: " + str(len(crawledData.crawled_urls)) + "::::::::::::::::::::::::\n" + crawled_urls
        data = {
                    "success": True,
                    "data": response
                }
        return JsonResponse(data)
    except Exception as e:
        data = {
            "success": False,
            "data": {"Something went wrong !!" + e}
        }
        return JsonResponse(data)


def clean_output(crawled_urls):
    output = ''
    for i in range(len(crawled_urls)):
        output = output + str(crawled_urls[i]) + "\n"
    return output
