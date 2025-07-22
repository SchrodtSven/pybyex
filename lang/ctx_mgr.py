# Context manager example
# 
#
# AUTHOR Sven Schrodt <sven@schrodt.club>
# SINCE 2025-07-10

class CtxMgr:
   def __enter__(self):
      print("Entering my context")
      return self

   def __exit__(self, exc_type, exc_value, traceback):
      print("Exiting my context")
        
with CtxMgr():
   print("Foo...")