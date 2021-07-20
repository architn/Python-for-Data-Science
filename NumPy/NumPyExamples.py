# NumPy is faster to read less bytes of memory compared to Python Lists, hence it is faster and consumes less memory
# No type checking when iterating through objects
# Uses contiguous memory - Effective Cache Utilization, SIMD Vector Processing
# Insertion, Deletion, Appending, concatenation all is supported both in NumPy and Py Lists

# Applications of NumPy:
# 1. MATLAB replacement
# 2. Plotting (Matplotlib)
# 3. Backend (Pandas, Connect 4, Digital Photography)
# 4. Machine Learning

import numpy as np

# Examples of Properties and Built-In Methods NumPy


def NumPyProperties():
    # How to convert a Python List to a NumPy
    my_list = [1, 2, 3]
    numpy_list = np.array(my_list)
    print(numpy_list)

    # Difference between Lists and NumPy
    # Lists:
    a = [1, 3, 5]
    b = [1, 2, 3]
    # If we try multiplying a * b, it will give an error.

    # NumPy:
    a = np.array([1, 3, 5])
    b = np.array([1, 2, 3])
    c = a * b
    print(c)

    # Initializing 2 Dimensional Arrays with NumPy
    sampleNumpyArray = np.array([[9.0, 8.5, 7.5], [6.0, 5.4, 6.3]])
    print(sampleNumpyArray)

    # Get Dimension of Array
    print("Dimension of Array is: {}".format(sampleNumpyArray.ndim))

    # Get shape of Array
    print("Shape of Array is: {}".format(sampleNumpyArray.shape))

    # Get Type
    print("Type of Array is: {}".format(sampleNumpyArray.dtype))

    # Set Type of NumPy Array
    secondNumpyArray = np.array([[9.0, 8.5, 7.5], [6.0, 5.4, 6.3]], dtype='int16')
    print("Type of Second Array is: {}".format(secondNumpyArray.dtype))

    # Get Item Size
    print("Item Size of Array is: {}".format(sampleNumpyArray.itemsize))

    # Get Size
    print("Size of Array is: {}".format(sampleNumpyArray.size))

    # Get Total Size ( Total Size = ItemSize * Size)
    print("Total Size of Array is: {}".format(sampleNumpyArray.nbytes))


# NumPyProperties()


# Examples of Accessing/Changing Specific Elements, Rows, Columns etc


def NumpyChangingElements():
    exampleNumpyArray = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
    print(exampleNumpyArray)

    # Get Shape
    print("Shape of Array is: {}".format(exampleNumpyArray.shape))

    # Get specific Element [row, column}
    # Example to get the value of 13 in the given NumPy array we will refer it:
    print(exampleNumpyArray[1, 5])
    # Important: Do not forget the zero indexing!

    # Get a specific row
    # Example to get the first, second row in the given NumPy array:
    print("First Row:")
    print(exampleNumpyArray[0, :])
    print("Second Row:")
    print(exampleNumpyArray[1, :])

    # Get a specific column
    # Example to get the first, second column in the given NumPy array:
    print("First Column:")
    print(exampleNumpyArray[:, 0])
    print("Second Column:")
    print(exampleNumpyArray[:, 1])

    # Change element
    exampleNumpyArray[1, 5] = 20
    print("Changed element in Numpy Array")
    print(exampleNumpyArray)

    # Change elements in second row
    exampleNumpyArray[1, :] = 5
    print("Changed second row in Numpy Array")
    print(exampleNumpyArray)

    # Change elements in second column
    exampleNumpyArray[:, 1] = 3
    print("Changed second column in Numpy Array")
    print(exampleNumpyArray)

    # 3 Dimensional Example
    threeDimensionalExample = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])

    # Get Specific Element in 3 - D Array (work outside in)
    print(threeDimensionalExample)
    # To get the value of 2 in 3-D Array:
    print(threeDimensionalExample[0, 0, 1])

    # Replace Element in 3-D Array
    threeDimensionalExample[:, 1, :] = [[9, 9], [8, 8]]
    print("Replacing elements in 3-D Array")
    print(threeDimensionalExample)


# NumpyChangingElements()


# Examples of Initializing Different Types of Arrays

def InitializingDifferentNumpyArrays():

    # Initializing all 0s array
    allZeroArray = np.zeros(5)
    print("All Zeroes Array")
    print(allZeroArray)
    allZeroArray1 = np.zeros((2, 3, 4, 5))
    print("Complex Zero Array")
    print(allZeroArray1)

    # Initializing 1s array
    allOneArray = np.ones((4, 2, 2), dtype='int32')
    print("All 1s Array")
    print(allOneArray)

    # Initializing Array with any other number
    anyNumberArray = np.full((2, 2), 99)
    print("An array with only 99s:")
    print(anyNumberArray)

    # Initializing an array of random numbers of decimals
    randomDecimalNumbersArray = np.random.rand(2, 2)
    print("Random decimals Number Numpy Array")
    print(randomDecimalNumbersArray)

    # Initializing an array of random numbers of decimals
    randomNumbersArray = np.random.randint(3, 7, size=(3, 3))
    print("Random Number Numpy Array")
    print(randomNumbersArray)

    # Initializing an Identity Matrix
    identityMatrix = np.identity(2)
    print("Identity Matrix")
    print(identityMatrix)

    # Be Careful while copying arrays
    a = np.array([1, 2, 3])
    b = a.copy()
    b[0] = 100
    print(b)
    print(a)


# InitializingDifferentNumpyArrays()

# Examples of Mathematical Operations using NumPy

def MathematicsWithNumpy():

    # Addition
    someArray = np.array([1, 2, 3])
    print("Adding two to array")
    print(someArray.copy()+2)

    # Subtraction
    print("Subtracting two to array")
    print(someArray.copy() - 2)

    # Multiplication
    print("Multiplying two to array")
    print(someArray.copy() * 2)

    # Division
    print("Dividing two to array")
    print(someArray.copy()/2)

    # Adding two Numpy arrays
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    result = array1 + array2
    print("Adding two Numpy arrays")
    print(result)

    # Raising values of Numpy arrays by 2
    originalArray = np.array([2, 3, 4])
    raisedToTwoArray = originalArray ** 2
    print("Raised to Two Array")
    print(raisedToTwoArray)


# MathematicsWithNumpy()

