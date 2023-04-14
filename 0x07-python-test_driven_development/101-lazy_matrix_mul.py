#!/usr/bin/python3
"""
module with 'lazy_matrix_mul'
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiply matrix using numpy """
    return np.dot(m_a, m_b)
