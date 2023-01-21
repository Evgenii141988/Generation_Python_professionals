def get_dict(nums: list) -> dict:
    if len(nums) == 2:
        return {nums[0]: nums[1]}
    else:
        return {nums[0]: get_dict(nums[1:])}


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    print(get_dict(numbers))
