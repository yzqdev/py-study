
import json



def stringToIntegerList(input):
    return json.loads(input)


def integer_list_to_string(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            A = stringToIntegerList(line);

            ret = Solution().sortedSquares(A)

            out = integer_list_to_string(ret);
            print(out)
        except StopIteration:
            break



if __name__ == '__main__':
    main()