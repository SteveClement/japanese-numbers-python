#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import six

class ParsedResult(object):

  def __init__(self, text=None, number=None, type=int, index=-1):
    self.text   = text
    self.number = number
    self.type   = type
    self.index  = index

  def __repr__(self):
    # __repr__ always returns a string type. We don't want to return bytes, thus we use six in __str__()
    return self.__str__()

  def __str__(self):
    # Consider python2 ppl, because easy to implement, for the rest, please use py3
    # See -> https://pythonclock.org/
    if six.PY2:
      return '<{0} {1[number]} : "{1[text]}" index={1[index]}>'. \
           format(self.__class__.__name__, self.__dict__).encode('utf8')
    return '<{0} {1[number]} : "{1[text]}" index={1[index]}>'. \
           format(self.__class__.__name__, self.__dict__)
