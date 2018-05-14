import re
from .base import Base

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'takkii'
        self.mark = '[dictionary]'
        self.input_pattern = (r'[^. *\t]\.\w*\|\h\w*::')

    def get_complete_position(self, context):
        m = re.search(r'\w*$', context['input'])
        return m.start() if m else -1


    def gather_candidates(self, context):
        dic = open("~/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete")
        reader = dic.read()
        dic.close()
        reader = reader.split("\n")
        for read_txt in dic :
        return read_txt