#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 00:30:31 2018

@author: jinyi
"""
# myapp.py
import logging
import mylib


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()
