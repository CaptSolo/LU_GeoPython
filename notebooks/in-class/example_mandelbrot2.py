import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def display_mandelbrot(real, imag, zoom):
    width, height = 800, 800
    max_iter = 512
    xmin, xmax = real - 1.5/zoom, real + 1.5/zoom
    ymin, ymax = imag - 1.5/zoom, imag + 1.5/zoom

    r1, r2, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

    plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    plt.colorbar()
    plt.title(f'Mandelbrot Set\nReal: {real}, Imaginary: {imag}, Zoom: {zoom}')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

if __name__ == "__main__":
    real = -0.047131370252400814 + 0.000001
    imag = -0.6449696900109125
    zoom = 1.4880649618e+6
    display_mandelbrot(real, imag, zoom)