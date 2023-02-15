from ListTree import Tree

tree = Tree('Drinks', [])

cold = Tree('Cold', [])
hot = Tree('Hot', [])

test = Tree('test', [])
fanta = Tree('Fanta', [test])


tree.addChild(cold)
tree.addChild(hot)
cold.addChild(fanta)

print(tree)

