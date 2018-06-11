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

#    When you execute a Python script,
#    it is treated as the main and its __name__ attribute is set to "__main__".
#    If you import this script as a module in another script,
#    the __name__ is set to the name of the script/module.


if __name__ == '__main__':
    main()
