__author__ = 'zhonghong'

class Index(object):

    # def __init__(self):
    #     self.load.model('test_model', 'tm')

    def index(self):
        return 'hello world'

    # def get_test_model(self):
    #     return self.tm.select()

    def get_arg(self):
        return self.input.get('arg1')

    def post_arg(self):
        # print self.input.environ, 'eeeee'
        # print int(self.input.environ.get('CONTENT_LENGTH', 0))
        # print self.input.environ['wsgi.input'].read(int(self.input.environ.get('CONTENT_LENGTH', 0)))
        return self.input.post('arg1')
