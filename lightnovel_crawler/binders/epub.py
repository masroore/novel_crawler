import logging
import os

from ebooklib import epub

logger = logging.getLogger('EPUB_BINDER')


def make_intro_page(crawler):
    html = '<div style="padding-top: 25%; text-align: center;">'
    html += '<h1>%s</h1>' % (crawler.novel_title or 'N/A')
    html += '<h3>%s</h3>' % (crawler.novel_author or 'N/A').replace(':', ': ')
    html += '</div>'
    return epub.EpubHtml(
        uid='intro',
        file_name='intro.xhtml',
        title='Intro',
        content=html,
    )


def make_chapters(book, chapters):
    book.toc = []
    for i, chapter in enumerate(chapters):
        xhtml_file = 'chap_%s.xhtml' % str(i + 1).rjust(5, '0')
        content = epub.EpubHtml(
            # uid=str(i + 1),
            file_name=xhtml_file,
            title=chapter['title'],
            content=chapter['body'] or '',
        )
        book.add_item(content)
        book.toc.append(content)


def bind_epub_book(app, chapters, volume=''):
    book_title = (app.crawler.novel_title + ' ' + volume).strip()
    logger.debug('Binding %s.epub', book_title)

    # Create book
    book = epub.EpubBook()
    book.set_language('en')
    book.set_title(book_title)
    book.add_author(app.crawler.novel_author)
    book.set_identifier(app.output_path + volume)

    # Create intro page
    intro_page = make_intro_page(app.crawler)
    book.add_item(intro_page)

    # Create book spine
    if app.book_cover:
        book.set_cover('image.jpg', open(app.book_cover, 'rb').read())
        book.spine = ['cover', intro_page, 'nav']
    else:
        book.spine = [intro_page, 'nav']

    # Create chapters
    make_chapters(book, chapters)
    book.spine += book.toc
    book.add_item(epub.EpubNav())
    book.add_item(epub.EpubNcx())

    # Save epub file
    epub_path = os.path.join(app.output_path, 'epub')
    file_path = os.path.join(epub_path, book_title + '.epub')
    logger.debug('Writing %s', file_path)
    os.makedirs(epub_path, exist_ok=True)
    epub.write_epub(file_path, book, {})
    logger.warning('Created: %s.epub', book_title)
    return file_path


def make_epubs(app, data):
    epub_files = []
    for vol in data:
        if len(data[vol]) > 0:
            book = bind_epub_book(app, volume=vol, chapters=data[vol])
            epub_files.append(book)

    return epub_files
