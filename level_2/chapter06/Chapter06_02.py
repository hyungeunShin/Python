# AsyncIO

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
# pip install beautifulsoup4
from bs4 import BeautifulSoup

start_time = timeit.default_timer()

urls = ['https://naver.com', 'http://daum.net', 'https://velog.io']

async def main():
    executor = ThreadPoolExecutor(max_workers=10)

    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    result = await asyncio.gather(*futures)
    print('Result : ', result)

async def fetch(url, executor):
    print('Thread Name :', threading.current_thread().name, 'Start', url)
    result = await loop.run_in_executor(executor, urlopen, url)
    soup = BeautifulSoup(result.read(), 'html.parser')
    # print(soup.prettify())
    print('Thread Name :', threading.current_thread().name, 'Done', url)
    return soup.title

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('Total Running Time : ', timeit.default_timer() - start_time)