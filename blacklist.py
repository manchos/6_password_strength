import urllib.request

blacklist_url = \
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt'


def load_content_from_urlfile(url=blacklist_url):
    blacklist_content = ''
    try:
        blacklist_content = urllib.request.urlopen(url)
    except ValueError:
        print("Oops!  That was no valid adress.  Try again...")
    return blacklist_content


def load_blacklist_from_content(blacklist_content):
    return [x.strip().decode('UTF-8') for x in blacklist_content]


def load_blacklist(url=blacklist_url):
    blacklist_content = load_content_from_urlfile(url)
    return load_blacklist_from_content(blacklist_content)


if __name__ == '__main__':
    content = load_content_from_urlfile()
    blacklist = load_blacklist_from_content(content)
    print(blacklist)

