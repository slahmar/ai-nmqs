# Salomé Lahmar 16201438

from node import Node

INFINITY = 1000

# Negamax variant of the alpha beta algorithm
def alpha_beta_negamax(node, depth, achievable = -INFINITY, hope = INFINITY, static_eval=0):
    if depth == 0:
        static_eval += 1
        print_static_evaluation(node, achievable, hope, depth)
        return (node.estimated, static_eval)
    else:
        score = -INFINITY
        for child in node.children:
            (temp, static_eval) = alpha_beta_negamax(child, depth-1, -hope, -achievable, static_eval)
            temp = -temp
            if temp >= hope:
                print_search_evaluation(node, achievable, hope, depth, temp)
                return (temp, static_eval)
            achievable = max(temp, achievable)
        print_search_evaluation(node, achievable, hope, depth, achievable)
        return (achievable, static_eval)
            
            
def print_static_evaluation(node, achievable, hope, depth):
    node.print_message(depth, achievable, hope, node.estimated, "static")

def print_search_evaluation(node, achievable, hope, depth, value):
    node.print_message(depth, achievable, hope, value, "search")

# Null move quiescence search variant of alpha-beta algorithm
def alpha_beta_nmq(node, depth, achievable = -INFINITY, hope = INFINITY, static_eval = 0):
    if depth == 0:
        (estimated_value, static_eval) = nmq_evaluation(node, -INFINITY, INFINITY, static_eval)
        return (estimated_value, static_eval)
    else:
        score = -INFINITY
        for child in node.children:
            (temp, static_eval) = alpha_beta_nmq(child, depth-1, -hope, -achievable, static_eval)
            temp = -temp
            if temp >= hope:
                return (temp, static_eval)
            achievable = max(temp, achievable)
        return (achievable, static_eval)

def nmq_evaluation(node, lower, upper, static_eval):
    best = node.estimated
    static_eval+=1
    for child in node.children:
        if best >= upper:
            return (best, static_eval)
        (temp, static_eval) = nmq_evaluation(child, -upper, -best, static_eval)
        temp = -temp
        best = max(best, temp)
    return (best, static_eval)