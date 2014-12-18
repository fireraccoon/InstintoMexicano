# Behaviour Trees 

## SELECTOR ==> FIRST SUCCESS ##
"""
*  check which child to run in priority order until the
*  first one succeeds or returns that it is running.
*  Order of child counts
*
*  SUCCESS : as soon as any of the children returns SUCCESS
*  FAILED  : if all children return FAILED
*  RUNNING : as soon as any of the children returns RUNNING
"""



## SEQUENCE ==> FIRST FAIL ## 
"""
* Child are evaluated one by one (from left to right)
* When it is finished, the next one is validated and executed
* If one fails, the Sequence fails
*
* SUCCESS : all children return SUCCESS
* FAILED  : as soon as any of the children returns FAILURE
* RUNNING : as soon as any of the children returns RUNNING
"""