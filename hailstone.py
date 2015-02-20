#!/usr/bin/python2.7

# Your Name
# Physics 91SI Spring 2013
# Lab #10, Part 1 

# Hailstone sequence analyzer

import sys
import numpy as np
from matplotlib import pyplot as plt

def hailstone(n):
    """Compute the Hailstone sequence starting at n"""
    seq = []
    while n != 1:
        seq.append(n)
        if n % 2 == 0: n = n/2
        else: n = 3*n + 1
    return seq


def get_peaks(seq):
    """Find the number of peaks in the given sequence"""
    # Your code goes here
    pass


def plot_seq(seq):
    """Plot a sequence and print the length of the sequence and number of
    peaks"""
    p1 = plt.plot(seq, label=str(seq[0]))[0]
    color = p1.get_color()
    # Use color=color as a kwarg to annotate if you want the colors to match
    ##
    # Your code goes here
    ##


def main():
    """Your main method should compute the hailstone sequences for a range of
    input values, and call your other functions to calculate and visualize the
    properties of these sequences."""
    if "-range" in sys.argv[1]:
        N = int(sys.argv[2])
        ns = range(1, N+1)

        ##
        # Your code goes here
        ##

        # Skeleton plotting code
        plt.figure()
        plt.subplot(1,2,1)
        plt.plot(ns, lengths, 'o')
        plt.title("Sequence Lengths")
        plt.subplot(1,2,2)
        plt.plot(ns, num_peaks, 'o')
        plt.title("Number of Peaks")

    else:
        n = int(sys.argv[1])
        plot_seq(hailstone(n))


if __name__ == '__main__':
    plt.ion()
    main()
