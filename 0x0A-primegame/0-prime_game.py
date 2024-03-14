#!/usr/bin/python3


def is_prime(n):
  """
  This function checks if a number is prime.
  Args:
      n: The number to check.
  Returns:
      True if the number is prime, False otherwise.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def remove_multiples(nums, prime):
  """
  This function removes the prime number and its multiples from the list.
  Args:
      nums: The list of integers.
      prime: The prime number to remove.
  """
  for i in range(len(nums) - 1, -1, -1):
    if nums[i] % prime == 0:
      del nums[i]


def play_round(nums):
  """
  This function simulates a single round of the game.
  Args:
      nums: The list of integers.
  Returns:
      The name of the player who loses the round (winner of the current round).
  """
  maria_turn = True
  while nums:
    if maria_turn:
      # Find a prime number in the list and remove it with its multiples
      for num in nums:
        if is_prime(num):
          remove_multiples(nums, num)
          break
      maria_turn = False
    else:
      # Ben's turn - similar logic as Maria's turn
      for num in nums:
        if is_prime(num):
          remove_multiples(nums, num)
          break
      maria_turn = True
  # Check who lost the round based on the empty list
  return "Ben" if maria_turn else "Maria"


def isWinner(x, nums):
  """
  This function determines the winner of the game played x rounds.
  Args:
      x: The number of rounds.
      nums: The list of integers (remains same for all rounds).
  Returns:
      The name of the player with the most wins ("Maria" or "Ben") or "None" for a tie.
  """
  maria_wins = 0
  ben_wins = 0
  for _ in range(x):
    # Play a round and update winner count
    winner = play_round(nums.copy())  # Copy the list to avoid modification across rounds
    if winner == "Maria":
      maria_wins += 1
    else:
      ben_wins += 1
  # Return winner based on win count
  if maria_wins > ben_wins:
    return "Maria"
  elif maria_wins < ben_wins:
    return "Ben"
  else:
    return None

