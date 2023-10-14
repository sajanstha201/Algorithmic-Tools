def majority_element_naive(elements):
    c=1
    for i in range(len(elements)-1):
        if elements[i]==elements[i+1]:
            c+=1
            if(c>int(len(elements)/2)):
                return 1
        else:
            c=1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    input_elements.sort()
    print(majority_element_naive(input_elements))