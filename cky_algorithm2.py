import sys, json
from collections import defaultdict


class cky_algo(object):
	def __init__(self):
		self.nonterminal_dict = defaultdict(int)
		self.unary_dict = defaultdict(int)
		self.unary_qml = defaultdict(float)
		self.binary_dict = defaultdict(int)
		self.binary_qml = defaultdict(float)
		self.word_count = defaultdict(int)
		self.rules = defaultdict(list)
		self.unary_special = defaultdict(list)
		self.binary_parents = defaultdict(list)
		self.no_parent = set()

	# initializes variables 
	def rule_count(self, file):
		count_file = open(file, 'r')
		for line in count_file:
			parts = line.split()
			# dict of all nonterminals
			if parts[1] == "NONTERMINAL":
				self.nonterminal_dict[(parts[2])] = int(parts[0])
				string = parts[2]
				if string.isalpha() == False:
					self.no_parent.add(string) 
			#all unary rules and word counts
			elif parts[1] == "UNARYRULE":
				rule = parts[2] + " " + parts[3]
				self.unary_dict[(rule)] = int(parts[0])
				word = parts[3]
				self.word_count[word] += int(parts[0])
				string = parts[2]
				if string.isalpha() or string == '.':
					self.no_parent.add(string) 
				else:
					beg = string.index("<")
					end = string.index(">")
					parent = string[beg+1:end]
					rules = self.unary_special[parent]
					rules.append(rule)
					self.unary_special[parent] = rules
			# all binary rules and set of all rules
			else:
				nonterm = parts[2]
				rule1 = parts[3]
				rule2 = parts[4]
				rule = nonterm + " " + rule1 + " " + rule2
				self.binary_dict[(rule)] = int(parts[0])
				tup = (rule1, rule2)
				self.rules[nonterm].append(tup)

				if rule1.isalpha() or rule1 == '.':
					self.no_parent.add(rule1) 
				else:
					beg = rule1.index("<")
					end = rule1.index(">")
					parent = rule1[beg+1:end]
					rules = self.binary_parents[parent]
					rules.append(rule)
					self.binary_parents[parent] = rules

				if rule2.isalpha() or rule2 == '.':
					self.no_parent.add(rule2) 
				else:
					beg = rule2.index("<")
					end = rule2.index(">")
					parent = rule2[beg+1:end]
					rules = self.binary_parents[parent]
					rules.append(rule)
					self.binary_parents[parent] = rules
		for item in self.binary_parents.iterkeys():
			print item + " " + self.binary_special[item]
			print '\n'
		#sys.exit()
		count_file.close()

	# calculates maximum liklihood estimates give a string of the rules
	def calc_ml(self, rule):
		parts = rule.split()
		if len(parts) == 3:
			nonterms = parts[0] + " " + parts[1] + " " + parts[2]
			rule_count = float(self.binary_dict[nonterms])
			term = float(self.nonterminal_dict[(parts[0])])
			return rule_count/term
		else:
			nonterms = parts[0] + " " + parts[1]
			rule_count = float(self.unary_dict[rule])
			term = float(self.nonterminal_dict[(parts[0])])
			return rule_count/term

	# puts all maximum liklihood estimates into dictionary
	def compute_ml(self):
		for rule in self.unary_dict.iterkeys():
			self.unary_qml[rule] = self.calc_ml(rule)
		for rule in self.binary_dict.iterkeys():
			self.binary_qml[rule] = self.calc_ml(rule)

	# executes cky algorithm
	def cky_algorithm(self, line):
		# temporary dicts for backpointers and pi
		bp = defaultdict()
		pi = defaultdict(float)
		sentence = line.strip().split()
		n = len(sentence)

		# initialization
		index = 0
		for word in sentence:
			orig_word = word
			max_p = -float('inf')

			# adjusts for rare word
			if self.word_count[word] < 5:
				word = '_RARE_'
			elif word not in self.word_count:
				word = '_RARE_'		

			# adjusts for proper indexing	
			index += 1
			for nonterm in self.nonterminal_dict.iterkeys():
				rule = nonterm + " " + word
				if rule in self.unary_qml.iterkeys():
					pi[(index, index, nonterm)] = float(self.unary_qml[rule])
				else: 
					pi[(index, index, nonterm)] = 0.0
				bp[(index, index, nonterm)] = (nonterm, orig_word)

		# recusrive algorithm
		for l in range(1, n):
			for i in range(1, (n-l + 1)):
				j = i + l

				# iterates through all existingn nonterminals
				for nonterm in self.nonterminal_dict.iterkeys():
					max_p = 0.0
					curr_bp = []
					all_rules = self.rules[nonterm]
					for item in all_rules:
						for s in range(i, j):
							Y = item[0]
							Z = item[1]
							rule = nonterm + " " + Y + " " + Z

							# only checks rules that exist
							if rule in self.binary_dict:
								qml =  self.binary_qml[rule]
								pi1 = pi[(i, s, Y)]
								pi2 = pi[(s+1, j, Z)]
								current = qml * pi1 * pi2
								if current > max_p:
									max_p = current
									curr_bp = [nonterm, bp[(i, s, Y)], bp[(s+1, j, Z)]]
					# set max pi and backpointer associated
					pi[(i, j, nonterm)] = max_p
					bp[(i, j, nonterm)] = curr_bp

		# return cases
		if pi[1, n, 'S'] <= 0:
			max_p = -float('inf')
			curr_bp = []
			for nonterm in self.nonterminal_dict.iterkeys():
				current = pi[(1, n, nonterm)]
				if current > max_p:
					max_p = current
					curr_bp = bp[1, n, nonterm]
					start = nonterm
			return self.generate_tree(curr_bp)
		else:
			return self.generate_tree(bp[(1, n, 'S')])

	# generates json format
	def generate_tree(self, bp):
		return json.dumps(bp)

	# outputs into output
	def write_tree(self, file):
		dev_file = open(file, 'r')
		for line in dev_file:
			sys.stdout.write(self.cky_algorithm(line))
			sys.stdout.write('\n')
		dev_file.close()

def usage():
    print """
    python cky_algorithm.py [count_file] [dev_data]
    """

if __name__ == "__main__":

    if len(sys.argv) != 3: # Expects two argument: original count file and training data file
        usage()
        sys.exit(2)
    cky = cky_algo()
    cky.rule_count(sys.argv[1])
    #cky.compute_ml()
    #cky.write_tree(sys.argv[2])