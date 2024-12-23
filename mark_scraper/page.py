class Page(object):
    def __init__(
            self,
            url: str = None,
            body: str = None,
            html: str = None,
            title: str = None):
        self.url = url
        self.body = body
        self.html = html
        self.title = title
