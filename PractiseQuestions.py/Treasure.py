from collections import Counter

def can_split_treasure(chest):
    total_value = sum(chest)
    if total_value % len(chest) != 0:
        return False, []

    target_value = total_value // len(chest)
    gem_counts = Counter(chest)
    split = []

    for _ in range(len(chest)):
        current_split = []
        current_value = 0

        for gem in gem_counts:
            if gem_counts[gem] > 0 and current_value + gem <= target_value:
                current_split.append(gem)
                gem_counts[gem] -= 1
                current_value += gem

                if current_value == target_value:
                    break

        if current_value != target_value:
            return False, []

        split.append(current_split)

    return True, split

# Example chests
chests = [
    [4, 4, 4],
    [27, 7, 20],
    [6, 3, 2, 4, 1],
    [3, 2, 7, 7, 14, 5, 3, 4, 9, 2]
]

for chest in chests:
    can_split, split = can_split_treasure(chest)
    if can_split:
        print(f"The treasure {chest} can be split between {len(split)} treasure seekers: {split}")
    else:
        print(f"The treasure {chest} cannot be split equally between treasure seekers.")
