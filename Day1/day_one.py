import numpy as np

# Part 1
def pair_sorted_columns(filename):
    data = np.loadtxt(filename)

    left = data[:, 0]
    right = data[:, 1]

    left_sorted = np.sort(left)
    right_sorted = np.sort(right)

    pairs = []
    for i in range(len(left_sorted)):
        pairs.append((left_sorted[i], right_sorted[i]))

    distances = [abs(left - right) for left, right in pairs]
    total_distance = sum(distances)
    
    print("\nTotal absolute distance:", int(total_distance))

# Part2
def calculate_similarity_score(filename):
    data = np.loadtxt(filename)
    
    left = data[:, 0].astype(int)
    right = data[:, 1].astype(int)
    
    total_score = 0
    for left_num in left:
        count = np.sum(right == left_num)
        score_contribution = left_num * count
        total_score += score_contribution
        
    print(f"\nTotal similarity score: {total_score}")

def main() -> None:
    pair_sorted_columns("input.txt")
    calculate_similarity_score("input.txt")

if __name__ == '__main__':
    main()