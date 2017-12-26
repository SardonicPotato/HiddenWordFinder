import enchant
import argparse
import re

parser = argparse.ArgumentParser(description='Find hidden words.')
parser.add_argument('--text', help='text file to scan', default="input.txt")
parser.add_argument('--output', help='list of output words', default="output.txt")
parser.add_argument('--min_length', help='min length of words', type=int, default=4)
parser.add_argument('--max_length', help='max length of words', type=int, default=15)
args = parser.parse_args()

with open(args.text) as file:
    raw_text = file.read()
    text = re.sub(r"\W+", "", raw_text).lower()

d = enchant.Dict("en_GB")
n = len(text)
results = set()

for start_pos in range(n):
    for word_length in range(args.min_length, args.max_length+1):
        end_pos = start_pos + word_length
        if end_pos > n:
            continue
        possible_word = text[start_pos:end_pos]
        if d.check(possible_word):
            results.add(possible_word)

with open(args.output, 'w') as file:
    for word in results:
        file.write(word + '\n')
