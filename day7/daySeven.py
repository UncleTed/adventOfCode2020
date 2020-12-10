from treelib import Node, Tree
import re

baggage_claim = Tree()
root = baggage_claim.create_node('baggage claim', 'baggage claim')

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


def find_existing_bag(tree, color):
    return list(tree.filter_nodes(lambda n: n.tag == color))

def find_existing_top_level_bag(tree, color):
    return tree.children(root.identifier)

with open("./short.txt", "r") as f:

    for line in f:
        print(line)
        split_line = line.rstrip().split('contain')
        outer_bag = bag_name(split_line[0])
        inner_bags = get_inner_bags(split_line[1])

        existing_bags = find_existing_bag(baggage_claim, outer_bag)
        if(len(existing_bags) > 0):
            for bag in existing_bags:
                for i in inner_bags:
                    baggage_claim.create_node(i, parent=bag.identifier)

        else:
            outer_bag_node = baggage_claim.create_node(outer_bag, parent = 'baggage claim')
            for i in inner_bags:
                inner_existing = find_existing_top_level_bag(baggage_claim, i)
                print(f'inner_existing {inner_existing}')
                if(len(inner_existing) > 0):
                    #tree.move(node, new_parent)
                    baggage_claim.move_node(inner_existing[0].identifier, outer_bag_node.identifier)
                # if inner already exists
                # move existing
                else:
                    baggage_claim.create_node(i, parent=outer_bag_node.identifier)
                
    baggage_claim.show()
    shiny = list(baggage_claim.filter_nodes(lambda n: n.tag == 'shiny gold bag'))
    print(f'shiny gold bags: {len(shiny)}')
    for child in baggage_claim.children('baggage claim'):
        pass
        # print(f'{child.tag} {baggage_claim.children(child.identifier)[0]}')