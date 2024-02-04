import timeit
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum_: int):
  count_coins = {}
  for coin in coins:
    count = sum_ // coin
    if count > 0:
      count_coins[coin] = count
    sum_ = sum_ - coin * count
  return count_coins

def find_min_coins(sum_):
  min_coins_required = [0] + [float("inf")] * sum_ 
  last_coin_used = [0] * (sum_ + 1)

  for s in range(1, sum_ + 1):
    for coin in coins:
      if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
        min_coins_required[s] = min_coins_required[s - coin] + 1
        last_coin_used[s] = coin

  count_coins = {}
  current_sum = sum_
  while current_sum > 0:
    coin = last_coin_used[current_sum]
    count_coins[coin] = count_coins.get(coin, 0) + 1
    current_sum = current_sum - coin

  return count_coins

if __name__ == '__main__':
  sum = 1356297
  print(f"Жадібний: {timeit.timeit(lambda: find_coins_greedy(sum), number=10): <10f} {find_coins_greedy(sum)}")
  print(f"Динамічний: {timeit.timeit(lambda: find_min_coins(sum), number=10): <10f} {find_min_coins(sum)}")
