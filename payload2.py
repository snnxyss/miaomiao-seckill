import requests


class payload:
    req = {
        'url': '',
        'headers': {},
        'data': '',
        'method': 'GET'
    }

    def __new__(cls, http):
        http = http.split('\n')

        url = http[0].split(' ')
        url = url[1:-1]
        url = ' '.join(url)

        data = http[http.index('') + 1:len(http)]
        data = '\n'.join(data)

        headers = {}
        for head in http[1:http.index('')]:
            i = head.index(':')
            headers[head[0:i]] = head[i + 1:len(head)].strip()

        cls.req['url'] = 'http://' + headers['Host'] + url
        cls.req['headers'] = headers
        cls.req['data'] = data
        cls.req['method'] = http[0][0:http[0].index(' ')]

        return cls

    def get(self):
        return requests.request(
            method=self.req['method'],
            url=self.req['url'],
            headers=self.req['headers'],
            data=self.req['data'])
