#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interactive value input"""
import os
import logging
import requests
from colorama import init as init_colorama
from .app import start_app
from .app.arguments import get_args, build_parser
from .app.display import description, epilog, debug_mode
from .assets.version import get_value as get_version

from .lnmtl import LNMTLCrawler
from .webnovel import WebnovelCrawler
from .wuxia import WuxiaCrawler
from .wuxiac import WuxiaCoCrawler
from .wuxiaonline import WuxiaOnlineCrawler
from .boxnovel import BoxNovelCrawler
from .readln import ReadLightNovelCrawler
from .novelplanet import NovelPlanetCrawler
from .lnindo import LnindoCrawler
from .idqidian import IdqidianCrawler
from .utils.crawler import Crawler
from .tests.crawler_app_test import run_tests

crawler_list = {
    'https://lnmtl.com/': LNMTLCrawler,
    'https://www.webnovel.com/': WebnovelCrawler,
    'https://wuxiaworld.online/': WuxiaOnlineCrawler,
    'https://www.wuxiaworld.com/': WuxiaCrawler,
    'https://www.wuxiaworld.co/': WuxiaCoCrawler,
    'https://boxnovel.com/': BoxNovelCrawler,
    'https://novelplanet.com/': NovelPlanetCrawler,
    'https://www.readlightnovel.org/': ReadLightNovelCrawler,
    'https://lnindo.org/': LnindoCrawler,
    'https://www.idqidian.us/': IdqidianCrawler,
}


def main():
    init_colorama()

    os.environ['version'] = get_version()

    description()
    build_parser()

    args = get_args()
    if args.log:
        os.environ['debug_mode'] = 'true'
        levels = [None, logging.WARN, logging.INFO, logging.DEBUG]
        logging.basicConfig(level=levels[args.log])
        debug_mode(args.log)
        print(args)

    requests.urllib3.disable_warnings(
        requests.urllib3.exceptions.InsecureRequestWarning)

    try:
        if args.test:
            run_tests()
        else:
            start_app(crawler_list)

    except Exception as err:
        if args.log == 3:
            raise err

    # end try

    epilog()


if __name__ == '__main__':
    main()
