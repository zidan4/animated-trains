
#Capitilize constants. VAR
# raturn 0 <= rate <= 5.  returns true if greater than or equals to 0 and less than or equals to 5

class Bank:
  MIN_BALANCE = 100
  def __init__(self, name, amount, balance):
    self.name = name
    self.amount = amount
    self._balance = balance

  def deposit(self, amount):
    if self._is_valid_amount(amount):
      self._balance += amount
    else:
      raise ValueError("Deposit amount should be positive")
    
  def _is_valid_amount( self, amount):
    return self.amount > 0
  
  def __log_transaction(self, amount):
    print(f"Logging trannsaction of amount: {amount} at {datetime.now()}")
