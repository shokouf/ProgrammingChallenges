__author__ = 'shokoufeh'

def solution(A, Target):
    processed = {}
    for i in range(0 , len(A)):
        if Target- A[i] in processed:
            return [processed[Target-A[i]]+1,i+1]
        processed[A[i]]= i


if __name__ == "__main__":
    A = [2,7,11,13]
    print solution(A, 9)