import numpy as np

# numpy function to carry out operations on a matrix
def calculate(list):
    array = np.array(list)
    if len(list) < 9:
        # If the list contains less than 9 items, raise a ValueError
        raise ValueError("List must contain nine numbers.")
    else:
        # If the list contains nine numbers, continue with the function
        pass

    # convert the flattened array to 3X3 matrix
    array.shape = ((3,3))

    calculations = {
        'mean': [np.mean(array, axis=0), np.mean(array, axis=1), np.mean(array)],
        'variance': [np.var(array, axis=0), np.var(array, axis=1), np.var(array)],
        'standard deviation': [np.std(array, axis=0), np.std(array, axis=1), np.std(array)],
        'max': [np.max(array, axis=0), np.max(array, axis=1), np.max(array)],
        'min': [np.min(array, axis=0), np.min(array, axis=1), np.min(array)],
        'sum': [np.sum(array, axis=0), np.sum(array, axis=1), np.sum(array)]
    }

    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))