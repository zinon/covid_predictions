import proc as xp

import xquery as xq

q0 = xq.Query("All Period", "Confirmed > 0 and Date < '2021-01-01'")

ld = xp.DataLoader(query = q0)

ld.reporter()
