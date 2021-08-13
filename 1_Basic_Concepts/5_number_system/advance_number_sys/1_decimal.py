"""
Example:
Below print function returns False. Because
# >>> decimal.Decimal(1.1+2.2)
Decimal('3.300000000000000266453525910037569701671600341796875')
# >>> decimal.Decimal(3.3)
Decimal('3.29999999999999982236431605997495353221893310546875')
# >>>
"""
print(2.2+1.1 == 3.3)

# To overcome above issue, follow below format
from decimal import Decimal as d
print((d('2.2')+d('1.1')) == d('3.3'))
