**********************
 The ``numpy`` library
**********************

Numpy is the go-to python library when it comes to working with n-dimensional arrays.
Almost all popular python libraries that handle n-dimensional arrays in python either allow exporting data as an numpy array or implement same interface.

Numpy-like libraries:

* Zarr – https://zarr.readthedocs.io/en/stable/
* Dask arrays – https://dask.org/

Examples of libraries with numpy integration:

* matplotlib – plotting utility for python https://matplotlib.org/
* Pillow – image processing libraries https://pillow.readthedocs.io/en/stable/
* scipy – numerically efficient routines https://www.scipy.org/scipylib/index.html
* scikit-learn – basic machine learning https://scikit-learn.org/stable/
* cython – optimising static compiler for python https://cython.org/
* Pandas (next classes) – dataframes for python https://pandas.pydata.org/

Preparation
###########

If the ``import numpy`` command causes an ``ImportError``, install the ``numpy`` library using the following command: ``pip install numpy``.
I also suggest to check if ``ipython`` is installed in your current environment (it should be if you already have used ``jupyter``).
This can be tested with ``import IPython``.

Basics
######
In comparison with python lists, numpy arrays have a fixed size and type (called ``dtype``).

.. code-block::

    >>> np.empty((3, 3), dtype=np.uint16)
    array([[    0,     0,     0],
           [36864, 31715, 60221],
           [ 2046, 57344,     2]], dtype=uint16)


Types
~~~~~
basic ``numpy`` uses primitive types.

=============================== ================================================
Type                            Description
=============================== ================================================
``bool``                        ``True`` or ``False`` stored as a single bit
``int``                         signed 32 or 64 bits int
``int8/16/32/64``               respectively 8/16/32/64 signed integer
``uint8/16/32/64``              respectively 8/16/32/64 unsigned integer
``float16``                     half precision float
``float32``                     single precision float
``float64`` or ``float``        double precision float
``complex64``                   complex number represented as two ``float32``
``complex128`` or ``complex``   complex number represented as two ``float64``
``object``                      arbitrary python object, rarely used
=============================== ================================================

Please be wary of bit overflow.

Creating arrays
###############

* ``array(object,dtype=None, *, copy=True, order='K', subok=False, ndmin=0)`` - create a numpy array from an object
* ``empty(shape, dtype=float, order='C')`` – empty array of given shape
* ``zeros(shape, dtype=float, order='C')`` – array of given shape filled with zeros
* ``ones(shape, dtype=float, order='C')`` – array of given shape filled with ones
* ``full(shape, fill_value, dtype=None, order='C')`` – array of given shape filled with ``fill_value``
* ``arange([start, ]stop, [step, ]dtype=None)`` - similar to ``range`` but returns an ``ndarray`` instance
* ``linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`` – evenly spaced numbers over a specified interval

Similar to lists, numpy arrays support slicing.

.. code-block:: python

    array = np.zeros(10, dtype=np.uint8)
    array[2] = 1
    array[3] = 2
    array[4:7] = [3, 4, 5]
    print(array)

Its also supports multiple position assignment.

.. code-block:: python

    array = np.zeros(10, dtype=np.uint8)
    array[2:7] = 1
    print(array)

Mathematical operations
#######################

By default, mathematical operations (``+``, ``-``, ``*``, ``**`` etc.) are done positionally.
A full list can be found here: https://numpy.org/doc/stable/reference/routines.math.html

Matrix operations (e.g. matrix multiplication) are implemented in the ``numpy.linalg`` module
https://numpy.org/doc/stable/reference/routines.linalg.html

Exercise 1
~~~~~~~~~~

Fix the code, so that all ``assert`` pass.

.. code-block:: python

    arr1 = []
    arr2 = []
    assert len(arr1) == 10
    assert len(arr2) == 10
    assert np.all(arr1 == 100)
    assert np.all(arr2 == 156)
    assert np.all(arr1 + arr2 == 0)

Array properties
################

* ``shape`` – a tuple with info on the shape of array
* ``size`` – the size of an array, equal to the product of ``shape`` elements
* ``dtype`` – data type used for storage
* ``T`` – transpose of array

Array manipulation
##################
Numpy has many functions for shape manipulation:

* ``reshape`` – change the shape. New array shape has to have same ``size``
* ``squeeze`` – remove one dimension from the shape
* ``flatten`` - a flat, 1-d copy of the array
* ``ravel`` – contiguous flattened array

* ``astype`` – allows to change array dtype

For more, read https://numpy.org/doc/stable/reference/routines.array-manipulation.html

Slicing
#######

Numpy arrays allow for slicing along multiple dimension. For example:

.. code-block:: python

    >>> import numpy as np
    >>> arr = np.zeros((4, 4), dtype=np.uin16)
    >>> arr
    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]], dtype=uint16)
    >>> arr[1:-1, 1:-1] = 1
    >>> arr
    array([[0, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 0]], dtype=uint16)
    >>> arr[:2, :2]
    array([[0, 0],
           [0, 1]], dtype=uint16)

Remember that ``arr[:2, :2]`` is faster than ``arr[:2][:2]``!

IO operations
#############

* ``loadtxt`` – load array from a text file
* ``savetxt`` – save array to a text file
* ``load`` – load data from a binary file (``.npy`` or ``.npz``)
* ``save`` – save array to an ``.npy`` binary file
* ``savez`` and ``savez_compressed`` – save multiple arrays to an uncompressed or compressed binary file.

More: https://numpy.org/doc/stable/reference/routines.io.html

Statistics
##########

* ``min``/``amin``
* ``max``/``amax``
* ``median``
* ``std``
* ``var``

More: https://numpy.org/doc/stable/reference/routines.statistics.html

Many numpy functions have an ``axis`` argument which allows specification of the axis along which the operation is to be applied

.. code-block:: python

    >>> import numpy as np
    >>> arr = np.random.uniform(size=(10, 20))
    >>> np.std(arr)
    0.289538402318112
    >>> np.std(arr, axis=1)
    array([0.28590859, 0.29832191, 0.29218063, 0.29722575, 0.26979703,
           0.24772888, 0.28394164, 0.24025019, 0.29967281, 0.32325727])

Exercise 2
~~~~~~~~~~

Load data from ``data/sample.csv``; calculate mean, median and std for each column separately.
Solve this using numpy and without numpy (or pandas etc.)

Measure the time of it execution (using ``%time`` magic or ``time()`` function from ``time`` module) for each case.

Masking
#######

Comparing two congruent numpy arrays or a numpy array with a number yields an array of ``bool``.

.. code-block:: python

    >>> np.arange(9) > 4
    array([False, False, False, False, False,  True,  True,  True,  True])

To use array comparisons in an ``if`` statement, convert it to ``bool`` using ``np.all`` or ``np.any``.
Instead of doing the following:

.. code-block:: python

    if arr1 == arr2:
        do_something()

do:

.. code-block:: python

    if np.all(arr1 == arr2):
        do_something()

or, even better:

.. code-block:: python

    if np.array_equal(arr1, arr2):
        do_something()

Boolean masks could be used for indexing an existing array.
Lets randomize 1000 variables from ``N(2, 1)`` and then change all values bellow 0 to 0.

.. code-block:: python

    >>> arr = np.random.normal(2, 1, size=1000)
    >>> np.sum(arr < 0)
    27
    >>> arr[arr < 0] = 0
    >>> np.sum(arr < 0)
    0

Exercise 3
~~~~~~~~~~
Load data from ``data/ex3_data.npy`` and filter out rows with ``nan`` values.
Report how many rows are dropped during filtration, globally and per column.

Exercise 4
~~~~~~~~~~
Load data from ``data/iris.csv`` using ``loadtxt`` from ``numpy``. 
Skip header and name columns.
For each column calculate: `mean`, `median` and `std` using `axis` parameter.

Exercise 5
~~~~~~~~~~
Load data from ``data/sample_treated.npz``. 
Assume that each row of the ``outputs`` array contains information about the size of some structure traced in time.
We would like to know which object grows doubles its size during observation.
