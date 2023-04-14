#!/usr/bin/python3
"""
module with lazy matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiply matrices with numpy"""
    return np.matmul(m_a, m_b)
