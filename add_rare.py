import sys
from collections import defaultdict

"""
Takes in count file and training data - 
Produces new training data with infrequent words replaced with _RARE_
"""

def find_rare(file):
    # to count words
    rare_dict = defaultdict(int)
    # set of infreq words
    rare_set = set()

    count_file = open(file, 'r')
    for line in count_file:
        parts = line.split()
        if parts[1] == "UNARYRULE":
            word = parts[3] # rare
            count = int(parts[0])
            rare_dict[word] += count

    for word, count in rare_dict.iteritems():
        if count < 5:
            rare_set.add(word)

    count_file.close()
    return rare_set

def print_rare(file, infreq_words):
    data_file = open(file, 'r')
    infreq_words = map(lambda word : '"' + word + '"]', infreq_words)
    tree = data_file.read()

    for word in infreq_words:
        tree = tree.replace(word, '"_RARE_"]')
    sys.stdout.write(tree)

    data_file.close()

def usage():
    print """
    python add_rare.py [count_file] [training_data]
    """

if __name__ == "__main__":

    if len(sys.argv) != 3: # Expects two argument: original count file and training data file
        usage()
        sys.exit(2)

    infreq = find_rare(sys.argv[1])
    print_rare(sys.argv[2], infreq)