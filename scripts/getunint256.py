from decimal import Decimal

amount_decimal = Decimal("1000000000000000000000000")
decimals = 18

uint256_burn_amount = int(amount_decimal * (10 ** decimals))
print(uint256_burn_amount)
# 1 million 1,000,000 × 10¹⁸ = 1000000000000000000000000
# 10 million 10,000,000 × 10¹⁸ = 10000000000000000000000000
# 10 Billion 1000000000000000000000000000

