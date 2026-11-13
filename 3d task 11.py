# Initialize a global balance
balance = 1000.0


def deposit(amount):
  """Deposits money by explicitly modifying the global balance variable."""
  global balance
  if amount > 0:
    balance += amount
    print(f"Deposited ₹{amount}. Updated global balance: ₹{balance}")
  else:
    print("Deposit amount must be positive.")


def check_local_balance():
  """Demonstrates that a local variable with the same name

  does not affect the global account balance.
  """
  balance = 500.0  # This creates a local variable 'balance'
  print(f"Inside local function scope, balance is: ₹{balance}")


# --- Testing the program ---
print(f"Initial global balance: ₹{balance}\n")

# Using the deposit function (modifies global state)
deposit(500)

print()
# Calling the local scope function
check_local_balance()

print(f"\nFinal global balance after local check (unchanged): ₹{balance}")