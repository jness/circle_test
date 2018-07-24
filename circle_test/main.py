import requests


def main():
    """
    Main function
    """

    res = requests.get('http://circleci.com')

    if res:
        return res.reason
    else:
        return res.reason


if __name__ == '__main__':
    main()
