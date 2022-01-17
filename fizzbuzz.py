class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''
        collect n
        create array, call it answer
        start i from 1 to n
        for each i
            if i is divisible by 3 and 5
                add "FizzBuzz" to answer array
            else if i is divisible by 3
                add "Fizz" to answer array
            else if i is divisible by 5
                add "Buzz" to answer array
            else
                add i as string to answer array

        return answer
        '''

        if n < 0:
            return []

        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer
