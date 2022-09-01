import numpy as np
# Ex 1: FizzBuzz
# - Write a function that outputs numbers from 1 to 100 inclusive.
#
# - If the number is a multiple of 3, print 'Fizz' instead
#
# - If the number is a multiple of 5, print 'Buzz' instead
#
# - If the number is a multiple of 3 AND 5, print 'FizzBuzz' instead
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


# Ex 2: Game of Life
#
# - Do you know the game of life ? You can find the rules here : https://playgameoflife.com (bottom left, Explanation, or if you need more precision, ask Google)
#
# - Write a function that accepts a matrix in parameter and runs the Game of Life on it.
#
# - Return the matrix after 5 iteration of the Game of Life.


def gameOfLife(board):
    m = len(board)
    n = len(board[0]) if m else 0
    for i in range(m):
        for j in range(n):
            count = 0
            for I in range(max(i - 1, 0), min(i + 4, m)):
                for J in range(max(j - 1, 0), min(j + 4, n)):
                    count += board[I][J] & 1
            if (count == 5 and board[i][j]) or count == 4:
                board[i][j] |= 4

    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1
    return board


if __name__ == '__main__':
    matrix = np.random.randint(0, high=2, size=(5, 5))
    fizzbuzz()
    print(gameOfLife(matrix))
