from itertools import count, cycle

class FizzBuzz:

    fizzer = cycle(['']*2 +  ['fizz'])
    buzzer = cycle(['']*4 +  ['buzz'])
    counter = count(start=1)

    def build_response(self, fizz, buzz, count):
        fizzbuzz = fizz + buzz
        if fizzbuzz:
            return fizzbuzz
        return str(count)

    def do_fizzbuzz_step(self):
        fizz = next(self.fizzer)
        buzz = next(self.buzzer)
        count = next(self.counter)
        output = self.build_response(fizz, buzz, count)
        yield output, count

    def play_game(self, n):
        print('Playing FizzBuzz')
        while True:
            fizzbuzz, count = next(self.do_fizzbuzz_step())
            print(fizzbuzz)
            if count >= n:
                break

def main():
    fizzbuzz = FizzBuzz()
    fizzbuzz.play_game(100)

if __name__ == '__main__':
    main()
