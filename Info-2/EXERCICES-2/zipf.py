import matplotlib.pyplot as plt

def zipf_plot(freqs):
    """ input:
            freqs: list of integers
        output:
            None
        display Zipf's graphics (see https://en.wikipedia.org/wiki/Zipf%27s_law)
    """
    n = sorted(freqs, reverse = True)
    plt.figure()
    plt.loglog()
    plt.plot(n)
    plt.show()

if __name__ == '__main__':
    zipf_plot([1, 1, 1, 1, 10, 10, 10, 100, 1000])
