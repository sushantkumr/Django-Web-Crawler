from urllib.parse import urljoin, urlparse


def is_link_internal(link, parent_url):
    # import pudb; pudb.set_trace();
    if parent_url[0:7] == "http://":
        parent_url = parent_url[7:]
    elif parent_url[0:8] == "https://":
        parent_url = parent_url[8:]
    if parent_url in link:
        return True
    else:
        return False


def is_url_valid(link):
    '''
    Reject a link if
        - empty
        - PDF or DOC
        - mailing links
    @input:
        link: Link present in the parent_url webpage
    @output:
        boolean: invalid or not
    '''
    if not link or any(ext in link for ext in ('.pdf', 'docx')) \
            or link.startswith('mailto:') or ('#' in link):
        return False
    else:
        return True


def get_clean_url(parent_url, link):
    '''
    Clean up url by
        - complete relative links
        - always start URL with 'http://'
        - remove trailing "/"
    @input:
        parent_url: URL being scraped
        link: Link present in the parent_url webpage
    @output:
        url: the clean url
    '''
    if(link[:2] == '//'):
        link = link[2:]

    if parent_url[0:4] != "http":
        parent_url = "http://" + parent_url

    if not bool(urlparse(link).netloc):
        link = urljoin(parent_url, link.strip())

    length_of_link = len(link)
    if link[length_of_link - 1] == '/':
        link = link[:length_of_link - 1]

    return link
