
1PROPERTIES OF SET AND DICTIONARY

   SET                                                                  DICTIONARY
  unordered elements                                            Stores data in key–value pairs.
  Mutable – you can add,Remove items.                           Keys must be unique and immutable
  Supports set operations like union,                           Ordered & mutable – you can add, update

2.ADD

g={12,18,19,20,21,"hello"}
print(g.add(100))
print(g)

3.UPDATE

g2={22,25}
print(g.update(g2))
print(g)

4.REMOVE

print(g.remove("hello"))
print(g)
