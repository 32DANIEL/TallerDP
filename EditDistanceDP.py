def longest_common_subsequence(permutation1, permutation2):
    dp = [[0] * (len(permutation2) + 1) for _ in range(len(permutation1) + 1)]

    for i in range(1, len(permutation1) + 1):
        for j in range(1, len(permutation2) + 1):
            if permutation1[i-1] == permutation2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]

def calculate_operations(N, permutation1, permutation2):
    lcs = longest_common_subsequence(permutation1, permutation2)
    return 2 * (N - lcs)

def main():
    T = int(input().strip())  
    for case in range(1, T + 1):
        N = int(input().strip())
        permutation1 = list(map(int, input().strip().split()))
        permutation2 = list(map(int, input().strip().split()))
        operations = calculate_operations(N, permutation1, permutation2)
        print(f'Caso-{case}: {operations}')

if __name__ == "__main__":
    main()
