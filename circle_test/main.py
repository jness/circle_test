import sys
import requests


def main():
    """
    Main function
    """

    url = 'http://circleci.com'

    if len(sys.argv) == 2:
        if 'http://' in sys.argv[1]:
            url = sys.argv[1]

    res = requests.get(url)

    if res:
        print('%s returned success: %s' % (url, res))
    else:
        print('%s returned error: %s' % (url, res))


if __name__ == '__main__':
    main()
