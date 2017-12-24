import test as tst

def function():
  print("this is two's function")
  tst.function()

if __name__ == "__main__":
  function()
else:
  print("two is being imported")
