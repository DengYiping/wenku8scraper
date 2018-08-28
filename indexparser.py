from parser import Parser
from urllib.parse import urljoin

class IndexParser(Parser):
    def parse(self):
        title = self.soup.find(id = 'title').string
        self.title = title

        tbs = self.soup.find_all('table', 'css')

        if len(tbs) == 0:
            raise ValueError('invalid page format as a index page')

        tb = tbs[0]
        trs = tb.find_all('tr')

        chapters = {}
        current = ''
        for tr in trs:
            # iterate over each line

            tds = tr.find_all('td')
            if len(tds) == 1 and 'vcss' in tds[0].get('class'):
                # if it is chapter line
                chapter_name = tds[0].string

                if chapter_name not in chapters:
                    chapters[chapter_name] = []
                    current = chapter_name

            elif len(tds) > 0:
                for td in tds:
                    if 'ccss' in td.get('class'):
                        a_tag = td.a
                        if a_tag is not None:
                            # if it is a page line
                            # make the full path
                            link = urljoin(self.url, a_tag['href'])
                            chapters[current].append((a_tag.string, link))
            # assign chapters
            self.chapters = chapters
