import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import fnmatch

import numpy as np
import pytest

from lasio import read, las

test_dir = os.path.dirname(__file__)

egfn = lambda fn: os.path.join(os.path.dirname(__file__), "examples", fn)
stegfn = lambda vers, fn: os.path.join(
    os.path.dirname(__file__), "examples", vers, fn)

def test_add_curve_duplicate():
    l = las.LASFile()
    a = np.array([1, 2, 3, 4])
    b1 = np.array([5, 9, 1, 4])
    b2 = np.array([1, 2, 3, 2])
    l.add_curve('DEPT', a)
    l.add_curve('B', b1, descr='b1')
    l.add_curve('B', b2, descr='b2')
    # assert l.keys == ['DEPT', 'B', 'B']
    assert [c.descr for c in l.curves] == ['', 'b1', 'b2']

def test_add_curve_multi_lasfiles():
    l1 = las.LASFile()
    l2 = las.LASFile()
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 9, 1, 4])
    c = np.array([2, 2, 7, 6])
    l1.add_curve('DEPT', a)
    l2.add_curve('DEPT', a)
    l1.add_curve('B', b)
    l2.add_curve('C', c)
    assert [i.mnemonic for i in l1.curves] == ['DEPT', 'B'] and [i.mnemonic for i in l2.curves] == ['DEPT', 'C']