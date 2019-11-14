#!/usr/bin/env python
import os
import sys
import getpass
# import ctypes
# import exodus
import matplotlib.pyplot as plt
import numpy as np

cwd = os.getcwd()
user_name = getpass.getuser()  # expect this to be 'chovey' or 'rjterps'


class PostProcField:

    def __init__(self, folder):
        home = os.getcwd()
        print('ProsProcField server initialized from folder' + str(home))
        # a = np.array([1, 2, 3])
        # print('numpy array a = ' + str(a))
        # b = np.array([4, 5, 6])
        # fix, ax = plt.subplots(nrows=1, figsize=(5, 5))
        # ax.plot(a, b)
        # plt.show()
        # c = np.array([20, 2, 7, 1, 34])
        # q0 = np.min(c)  # min, zeroth quartile
        # q1 = np.quantile(c, 0.25)  # first quartile
        # q2 = np.quantile(c, 0.50)  # second quartile, median
        # q3 = np.quantile(c, 0.75)  # third quartile
        # q4 = np.max(c)  # max
        # print('Zeroth quartile = ' + str(q0))
        # print('First quartile = ' + str(q1))
        # print('Second quartile = ' + str(q2))
        # print('Third quartile = ' + str(q3))
        # print('Max = ' + str(q4))

    def quartiles(self, array):
        q0 = np.min(array)
        q1 = np.quantile(array, 0.25)  # first quartile
        q2 = np.quantile(array, 0.50)  # second quartile, median
        q3 = np.quantile(array, 0.75)  # third quartile
        q4 = np.max(array)  # max
        print('Zeroth quartile = ' + str(q0))
        print('First quartile = ' + str(q1))
        print('Second quartile = ' + str(q2))
        print('Third quartile = ' + str(q3))
        print('Max = ' + str(q4))
        return q0, q1, q2, q3, q4


if __name__ == "__main__":

    try:

        # os.system('module purge')
        # os.system('module load seacas')
        # os.system('module list')
        # import exodus
        pp = PostProcField(sys.argv[1])

    except IndexError as error:
        print('Error' + str(error))
        print('Error: no input folder target specified.')
        help_string = './pfield.py <input_folder>'
        print('Check script pattern: ' + help_string)
        sys.exit()  # early return because no target folder specified


