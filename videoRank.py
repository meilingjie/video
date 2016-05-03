# coding:utf-8

import operator
import urllib2

from bs4 import BeautifulSoup


def rank_video():
    dict = {}
    url = 'http://www.huya.com/g/dota2'
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content, "html.parser")

    video_all = soup.find_all('li', class_='video-list-item')
    for video in video_all:
        video_info = video.find('a', 'video-info')
        video_href = video_info.get('href')
        rank_content = video.find('i', 'js-num')
        rank = rank_content.get_text()
        dict[video_href] = int(rank)

    sorted_dict = sorted(dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    print sorted_dict

rank_video()
