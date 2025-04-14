import numpy as np

def calculate(list):
    validateList(list)
    
    flattened = np.array(list)
    matrixData = np.reshape(list, (3, 3))
    mean = [matrixData.mean(axis=0).tolist(), matrixData.mean(axis=1).tolist(), flattened.mean()]
    variance = [matrixData.var(axis=0).tolist(), matrixData.var(axis=1).tolist(), flattened.var()]
    standardDeviation = [matrixData.std(axis=0).tolist(), matrixData.std(axis=1).tolist(), flattened.std()]
    maxData = [matrixData.max(axis=0).tolist(), matrixData.max(axis=1).tolist(), flattened.max()]
    minData = [matrixData.min(axis=0).tolist(), matrixData.min(axis=1).tolist(), flattened.min()]
    sumData = [matrixData.sum(axis=0).tolist(), matrixData.sum(axis=1).tolist(), flattened.sum()]
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': standardDeviation,
        'max':maxData,
        'min':minData,
        'sum':sumData
    }


def validateList(data):
    if not isinstance(data, (list)):
        raise TypeError(f"Expected a list, but got {type(data).__name__}")
    if data == []:
        raise ValueError('data is empty')
    if len(data) != 9:
        raise ValueError('List must contain nine numbers.')
    try:
        reshape = np.reshape(data, (3, 3))
    except:
        raise ValueError('Length of data must be value of multiplication by three')
    for dt in data:
        if not isinstance(dt, (int, float)):
            raise TypeError(f"Expected a numeric value (int or float), but got {type(dt).__name__}")


    