#!/usr/bin/env micropython

class fileeditor:
    def __init__(self, filename = None):
        self.filename = filename
        self.contents = list()
        if filename is not None:
            self.load(filename)
    def help(self):
	print('''__init__(self, filename = None):
	      load(self, filename):
	      def save(self):
	      def print(self):
	      def append(self, line):
	      def insert(self, location, lines):
	      def strike(self, line)
	      ''')
	      
    def load(self, filename):
        self.filename = filename
	cnt = 0
        with open(filename,'r') as f:
            for cnt, line in enumerate(f):
                print('{}:\t{}'.format(cnt,line[:-1]))
                self.contents.append(line[:-1])
        return cnt

    def save(self):
        assert(self.filename is not None)
        with open(self.filename,'w') as f:
            [ (f.write(ln), f.write('\n')) for ln in self.contents ]

    def print(self):
        for cnt,line in enumerate(self.contents):
            print('{}:\t{}'.format(cnt,line)) 

    def append(self, line):
        self.contents.append(line)

    def insert(self, location, lines):
        self.contents = self.contents[:location] + lines + self.contents[location:]
    def strike(self, line):
        self.contents = self.contents[:line] + self.contents[line+1:]

#b = fileeditor('boot.py')
#b.print()
#b.append('#Hello')
#b.insert(3,['#World'])
#b.strike(2)
#b.print()
#b.save()
