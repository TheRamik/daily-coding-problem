#Problem 189
#Given an array of elements, return the length of the longest subarray where all its elements are distinct.
#For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

# Count # of tests pass
def runTests():
    results = []
    results.append(genericTestCase('initial test case', [5, 1, 3, 5, 2, 3, 4, 1], 5))
    results.append(genericTestCase('second test case', [1, 2, 4, 4, 5, 6, 7, 8, 3, 4, 5, 3, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4], 8))
    passedTest = 0
    for test in results:
        if test:
            passedTest += 1
        
    print('{}/{} tests passed'.format(passedTest, len(results)))


# Test Case
def genericTestCase(name: str, given: [int], expected: int):
    given = [5, 1, 3, 5, 2, 3, 4, 1]
    results = numOfDistinctElements(given)
    if results == 5:
        print('initialTestCase passed.')
        return True
    print('initialTestCase failed.')
    return False

def testCaseTwo():
    given = [1, 2, 4, 4, 5, 6, 7, 8, 3, 4, 5, 3, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4]
    results = numOfDistinctElements(given)
    if results == 8:
        print('testCaseTwo passed.')
        return True
    print('testCaseTwo failed.')
    return False

# Function without Sets
def numOfDistinctElements(given: [int]) -> int: 
    results = 0
    distinctElements = []
    for element in given:
        if element not in distinctElements:
            distinctElements.append(element)
    results = len(distinctElements)
    return results

if __name__ == "__main__":
    runTests()