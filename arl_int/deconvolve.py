#
#    ICRAR - International Centre for Radio Astronomy Research
#    (c) UWA - The University of Western Australia, 2016
#    Copyright by UWA (in the framework of the ICRAR)
#    All rights reserved
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston,
#    MA 02111-1307  USA
#
from arl.image.deconvolution import deconvolve_cube, restore_cube
from arl.image.operations import show_image
from .common import load, dump, params

from matplotlib import pyplot as plt
import sys

def main():
    dirty = load(2)
    psf = load(1)

    comp, residual = deconvolve_cube(dirty, psf, niter=1000, threshold=0.001,
    fracthresh=0.01, window='quarter', gain=0.7, scales=[0, 3, 10, 30])

    restored = restore_cube(comp, psf, residual)

    fig = show_image(comp)
    plt.title('Solution')
    fig.savefig('%s_Sol.png' % sys.argv[5])

    fig = show_image(residual)
    plt.title('Residual')
    fig.savefig('%s_Residual.png' % sys.argv[6])

    fig = show_image(restored)
    plt.title('Restored')
    fig.savefig('%s_Restored.png' % sys.argv[7])

    dump(3, comp)
    dump(4, residual)

if __name__ == '__main__':
    main()
