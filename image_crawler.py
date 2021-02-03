"""
This module crawls image files on the web.
"""

import os
import argparse

# 2021/02/03
# Google Image Crawler is not used because an error occurs due to a change in Google specifications.

from icrawler.builtin import BaiduImageCrawler, BingImageCrawler  # , GoogleImageCrawler

CRAWLER_CLASSES = {
    # 'google': GoogleImageCrawler,
    'bing': BingImageCrawler,
    'baidu': BaiduImageCrawler,
}

DEFAULT_OUT_DIR = './output/'
DEFAULT_MAX_NUM = 300
# DEFAULT_SEARCH_ENGINE = 'google'
DEFAULT_SEARCH_ENGINE = 'bing'
# DEFAULT_CRAWLER_CLASS = GoogleImageCrawler
DEFAULT_CRAWLER_CLASS = BingImageCrawler
DOWNLOADER_THREADS = 4


def crawl(keywords: list, out_dir: str = DEFAULT_OUT_DIR, max_num: int = DEFAULT_MAX_NUM,
          search_engine: str = DEFAULT_SEARCH_ENGINE):
    """
    Crawls image file.

    :param keywords: keywords for files to crawl
    :param out_dir: output files directory
    :param max_num: max number of files to crawl
    :param search_engine: search engine used for crawl
    """

    for keyword in keywords:
        crawler = get_crawler(search_engine, os.path.join(out_dir, keyword))
        crawler.crawl(keyword=keyword, max_num=max_num)


def get_crawler(crawler_op: str, out_dir: str):
    crawler_cls = CRAWLER_CLASSES.get(crawler_op.lower(), DEFAULT_CRAWLER_CLASS)
    return crawler_cls(downloader_threads=DOWNLOADER_THREADS, storage={'root_dir': out_dir})


# for command line
if __name__ == '__main__':
    # get parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keywords', nargs='*', required=True)
    parser.add_argument('-o', '--out-dir', default=DEFAULT_OUT_DIR)
    parser.add_argument('-m', '--max-num', type=int, default=DEFAULT_MAX_NUM)
    parser.add_argument('-s', '--search-engine', choices=CRAWLER_CLASSES.keys(), default=DEFAULT_SEARCH_ENGINE)
    args = parser.parse_args()

    print('processing...')
    crawl(args.keywords, args.out_dir, args.max_num, args.search_engine)
    print('finished!')
