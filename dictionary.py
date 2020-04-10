import requests


def translate(to_search):

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}

    data = {}
    data['i'] = to_search
    data['doctype'] = 'json'

    res = requests.post(url, data=data, headers=head)
    result = res.json()['translateResult'][0][0]['tgt']
    return result


if __name__ == '__main__':
    print(translate("hello"))
