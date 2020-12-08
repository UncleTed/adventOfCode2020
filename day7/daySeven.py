from treelib import Node, Tree
import re

def bag_name(t):
    return t.lstrip().rstrip().replace('bags', 'bag').rstrip('.')

def get_inner_bags(t):
    if t == ' no other bags.':
        return []
    else:
        inner_bags = []
        for inside in t.split(','):
            how_many = re.search(r"\d+",inside)
            inner_bags.append(bag_name(inside[how_many.end():]))
        return inner_bags

with open("./short.txt", "r") as f:
    baggage_claim = Tree()
    baggage_claim.create_node('baggage claim', 'baggage claim')
    for line in f:
        split_line = line.rstrip().split('contain')
        outer_bag = bag_name(split_line[0])
        inner_bags = get_inner_bags(split_line[1])

        existing_bags = list(baggage_claim.filter_nodes(lambda n: n.tag == outer_bag))
        if(len(existing_bags) > 0):
            for bag in existing_bags:
                for i in inner_bags:
                    baggage_claim.create_node(i, parent=bag.identifier)

        else:
            outer_bag_node = baggage_claim.create_node(outer_bag, parent = 'baggage claim')
            for i in inner_bags:
                baggage_claim.create_node(i, parent=outer_bag_node.identifier)
                
    baggage_claim.show()
    for child in baggage_claim.children('baggage claim'):
        pass
        # print(f'{child.tag} {baggage_claim.children(child.identifier)[0]}')