# # Different ways of using functions in module
# import pizza

# print('..........................................................')
# pizza.make_pizza(18, 'pepperoni')
# pizza.make_pizza(16, 'mushroom', 'green peppers', 'extra cheese')

# from pizza import make_pizza
# make_pizza(16, 'peperoni')
# make_pizza(20, 'mushroom', 'greenpeppers', 'extra cheese')

# from pizza import make_pizza as mp

# mp(16, ' peperoni')
# mp(19, 'mushroom', 'greenpepper', 'extra cheese')

# import pizza as p 

# p.make_pizza(21, 'peperoni')
# p.make_pizza(25, 'mushroom', 'greenpepper', 'extra cheese')

from pizza import*

make_pizza(51, 'peperoni')
make_pizza(56, 'mushroom', 'greenpepper', 'extra cheese')