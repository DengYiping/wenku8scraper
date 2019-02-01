from indexparser import IndexParser
from pageparser import PageParser
import sys
from ebooklib import epub
import mkepub

def main():
    # checking the arguments to make sure
    if len(sys.argv) != 2:
        print('wrong number of argument, should only contain the index url')
        exit(-1)

    # first argument - the index page
    index = IndexParser(sys.argv[1])
    index.parse()
    for chapter in index.chapters:
        book_name = f'{index.title} - {chapter}'
        print('-----------')
        print(f'download book: {book_name}')
        print(f'in total {len(index.chapters[chapter])}')

        book = mkepub.Book(title = book_name)

        sub_chapters = index.chapters[chapter]

        for sub_chapter, link in sub_chapters:
            print(f'download chapter: {sub_chapter}')
            page = PageParser(link)
            page.parse()
            book.add_page(title = sub_chapter, content = f'<h1>{sub_chapter}</h1><br/>{page.text}')

        book.save(f'{book_name}.epub')
        print(f'file generated for {book_name}')

if __name__ == '__main__':
    main()
