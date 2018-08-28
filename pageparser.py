from parser import Parser

class PageParser(Parser):
    def parse(self):
        content = self.soup.find_all(id = 'content')[0]
        lines = []
        for l in content.contents:
            if l.name == 'br':
                lines.append('<br/>')
            elif not l.name == 'ul':
                l_str = l.string
                if l_str is not None:
                    lines.append(str(l.string))
        self.text = ''.join(lines)
