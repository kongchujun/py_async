from qpython import qconnection
import pandas as pd
import numpy as np
np.bool = np.bool_

# connection to kdb+
q = qconnection.QConnection(host='localhost',port=8090, pandas=True)
q.open()

# # execute query
result = q.sendSync('sp')

print(result)

q.close()
