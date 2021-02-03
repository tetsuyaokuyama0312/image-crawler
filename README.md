# image-crawler
This tool crawls image files on the web.

## How to use
### 1. Install icrawler
- `pip install icrawler`

### 2. Run
- `python image_crawler.py [options]`

    - Options are as follows:

        |option name|abbreviation|description|required|default|choices|
        | ---- | ---- | ---- | ---- | ---- | ---- |
        |--keywords|-k|keywords for files to crawl|Y|-|-|
        |--out-dir|-o|output files directory|N|./output/|-|
        |--max-num|-m|max number of files to crawl|N|300|-|
        |--search-engine|-s|search engine used for crawl|N|bing|bing, baidu *|

       - `*` google is currently unavailable because icrawler does not support google specification changes
