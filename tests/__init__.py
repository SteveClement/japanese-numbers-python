#!/usr/bin/env python3
# -*- encoding:utf-8 -*-


from nose.tools import ok_
from nose.tools import eq_
from nose.tools import raises
from nose.tools import with_setup


def compare_result(a, b):
  eq_(a.number, b.number)
  eq_(a.text, b.text)
  eq_(a.index, b.index)
