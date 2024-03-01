def edit_distance_dc(permutation1, permutation2):

    def recurse(index1, index2):
        if index1 == len(permutation1):
            return len(permutation2) - index2
        if index2 == len(permutation2):
            return len(permutation1) - index1

        if permutation1[index1] == permutation2[index2]:
            return recurse(index1 + 1, index2 + 1)

        insert_cost = 1 + recurse(index1, index2 + 1)
        delete_cost = 1 + recurse(index1 + 1, index2)
        return min(insert_cost, delete_cost)
    return recurse(0, 0)

def main():
    T = int(input().strip()) 
    for case in range(1, T + 1):
        N = int(input().strip())  
        permutation1 = list(map(int, input().strip().split()))
        permutation2 = list(map(int, input().strip().split()))
        operations = edit_distance_dc(permutation1, permutation2)
        print(f'Caso-{case}: {operations}')

if __name__ == "__main__":
    main()
