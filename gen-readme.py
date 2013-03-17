#!/usr/bin/env python

from sys import version_info

if version_info[0] < 3:
    from urllib import quote
else:
    from urllib.request import quote


from glob import glob
import json

header = '''
Place for everything Pandas.

Lessons
-------
'''



format_item = '* [{name}]({url})'.format
bb_url = 'bitbucket.org/hrojas/learn-pandas/raw/master/lessons/{}'.format


def notebooks():
    return glob('lessons/*Lesson.ipynb')


def lesson_name(filename):
    with open(filename) as fo:
        return json.load(fo)['metadata']['name']


def nb_url(filename):
    raw_url = bb_url(quote(filename))
    return 'http://nbviewer.ipython.org/urls/{}'.format(raw_url)


def write_readme(nblist, fo):
    fo.write('{}\n'.format(header))
    for nb in nblist:
        name = lesson_name(nb)
        url = nb_url(nb)
        fo.write('{}\n'.format(format_item(name=name, url=url)))


def main():
    nblist = notebooks()
    with open('README.md', 'w') as fo:
        write_readme(nblist, fo)


if __name__ == '__main__':
    main()


