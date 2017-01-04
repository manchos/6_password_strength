import urllib.request

fileurl = \
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt'


def load_blacklist_from_urlfile(url):
    content = ''
    try:
        content = urllib.request.urlopen(url)
    except ValueError:
        print("Oops!  That was no valid adress.  Try again...")
    # with open(filepath, mode='r', encoding='utf8') as file_handler:
    return [x.strip().decode('UTF-8') for x in content]

blacklist = load_blacklist_from_urlfile(fileurl)

if __name__ == '__main__':
    print(blacklist)
    pass
