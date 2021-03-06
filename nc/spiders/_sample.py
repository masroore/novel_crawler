# -*- coding: utf-8 -*-
"""
Use this sample to create new sources
"""
import logging
from .crawler import Crawler

# TODO: Set this to your crawler name for meaningful logging
logger = logging.getLogger('CHANGE_THIS_NAME')


# TODO: Copy this file directly to your new crawler. And fill up
#       the methods as described in their todos

class SampleCrawler(Crawler):
    def initialize(self):
        # TODO: Initiaze your crawler, variables etc. It gets called at the
        #       beginning of the core.
        pass

    def dispose(self):
        # TODO: Dispose your crawler, variables etc. It gets called at the
        #       beginning of the core.
        pass

    @property
    def supports_login(self):
        '''Whether the crawler supports login() and logout method'''
        # TODO: Pass False or delete this method if this crawler
        #       does not support login.
        return False

    def login(self, email, password):
        # TODO: You can just delete this method if not necessary.
        #       You can use `self.get_response` and `self.submit_form`
        #       methods from the parent class. They maintain cookies
        #       automatically for you.
        pass

    def logout(self):
        # TODO: Logout from the site. Not that necessary, but still it is
        #       nice to logout after you are done.
        pass

    def read_novel_info(self, url):
        '''Get novel title, autor, cover etc'''
        # TODO: This method must be implemented to get the `novel_title`.
        #       You may or may not set the novel_cover, novel_author, volumes
        #       and chapter list, but the `novel_title` must be set here.
        pass

    def download_chapter_list(self):
        '''Download list of chapters and volumes.'''
        # TODO: Use this method if you need to retrieve chapter list from
        #       online. If you already got chapter list inside the method
        #       `read_novel_info`, implementing this one is not necessary.
        pass

    def get_chapter_index_of(self, url):
        '''Return the index of chapter by given url or -1'''
        # TODO: A default behavior has been implemented in the parent class.
        #       Delete this method if you want to use the default one.
        #       By default, it returns the first index of chapter from the
        #       `self.chapters` that has 'url' property matching the given `url`.
        pass

    def download_chapter_body(self, chapter):
        '''Download body of a single chapter and return as clean html format.'''
        # TODO: This method must be implemented. Return an empty body if
        #       something goes wrong. You should not return None.
        pass
