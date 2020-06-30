import pandas as pd
import numpy as np

xlsx_data= pd.read_excel("./list_1.xlsx", error_bad_lines=False)
xlsx_data = np.array(xlsx_data)

