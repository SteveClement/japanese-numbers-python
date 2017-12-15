#!/usr/bin/env python3
# -*- encoding:utf-8 -*-



class ParsedResult(object):

  def __init__(self, text=None, number=None, type=int, index=-1):
    self.text = text
    self.number = number
    self.type = type
    self.index = index

  def __repr__(self):
    return self.__str__()

  def __str__(self):
    return '<{0} {1[number]} : "{1[text]}" index={1[index]}>'. \
           format(self.__class__.__name__, self.__dict__).encode('utf8')
