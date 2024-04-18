import numpy as np
import scipy

x = np.array([[0.1, 0.2, 0.1, 0.1, 0.0],
              [0.8, 0.9, 1.0, 1.0, 0.9],
              [1.0, 1.0, 1.0, 1.0, 1.0],
              [0.9, 1.0, 1.0, 0.8, 1.0],
              [0.0, 0.1, 0.1, 0.2, 0.0]])

W = np.array([[1.0, 1.0, 1.0],
              [0.0, 0.0, 0.0],
              [-1.0, -1.0, -1.0]])

def correlate2d(x, W):
    window = np.lib.stride_tricks.sliding_window_view(x, W.shape)
    b = window * W
    ans = np.sum(b, axis=(2,3))
    return ans

def convolve2d(x, W):
    window = np.lib.stride_tricks.sliding_window_view(x, W.shape)
    b = window * np.rot90(W, 2)
    ans = np.sum(b, axis=(2,3))
    return ans

print(correlate2d(x, W))
print(scipy.signal.correlate2d(x, W, mode='valid'))
print("---------")
print(convolve2d(x, W))
print(scipy.signal.convolve2d(x, W, mode='valid'))