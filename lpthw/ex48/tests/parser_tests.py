import imp
from nose.tools import *
from ex48 import parser


def test_peek():
    assert_equal(parser.peek([('verb', 'run')]), 'verb')
