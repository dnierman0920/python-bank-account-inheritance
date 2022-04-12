class BankAccount:
  def __init__(self, balance=0):
    self.balance = balance
    self.interest_rate = 0.02

  def deposit(self, deposit_amount):
    if(deposit_amount >= 0):
      self.balance += deposit_amount
      return self.balance
    else:
      return False

  def withdraw(self, withdraw_amount):
    if(withdraw_amount >= 0):
      self.balance -= withdraw_amount
      return self.balance
    else:
      return False
  
  def accumulate_interest(self):
    self.balance *= (1 + self.interest_rate)
    return self.balance


class ChildrensAccount(BankAccount):
    def __init__(self):
      super().__init__()
      self.interest_rate = 0

    def accumulate_interest(self):
      self.balance += 10

class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.overdraft_penalty = 40

  def withdraw(self, withdraw_amount):
    if(withdraw_amount >= 0 and withdraw_amount < self.balance):
      self.balance -= withdraw_amount
      return self.balance
    else:
      self.balance -= self.overdraft_penalty
      return False

  
  def accumulate_interest(self):
    if (self.balance > 0):
      self.balance *= (1 + self.interest_rate)
      return self.balance

  
basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
