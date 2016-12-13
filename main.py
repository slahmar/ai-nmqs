# Salomé Lahmar 16201438

from generate_tree import generate_tree
from node import Node
from alpha_beta_variants import alpha_beta_negamax, alpha_beta_nmq

branching = 4
height = 8
inaccuracy = 4
spread = 4
infinity = 1000

# This will generate one tree and test both algorithms on this tree at all depths from 0 to height
valueString = input('Enter top node value: ')
value = int(valueString)
root = generate_tree(branching, height, value, inaccuracy, spread)
root.print_tree(height)

for depth in range(0, height+1):
	print("---------- Depth {} -----------".format(depth))
    (nega_value, nega_static_eval) = alpha_beta_negamax(root, depth)
    print("Simple alpha beta : value found = {} with {} static evaluations".format(nega_value, nega_static_eval))
    (nmq_value, nmq_static_eval) = alpha_beta_nmq(root, depth)
    print("NMQS : value found = {} with {} static evaluations".format(nmq_value, nmq_static_eval))
