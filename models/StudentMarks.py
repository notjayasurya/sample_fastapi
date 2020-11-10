import numpy as np
import pandas as pd
import random

index_list=[i for i in range(0,100)]
indexlist=np.array(index_list)

hours_of_study=[round(np.random.uniform(5,30),1) for i in range(0,100)]

Diversity_of_Skills=[random.randint(1,10) for i in range(0,100)]

Technical_knowledge=[random.randint(1,10) for i in range(0,100)]

Dedication=[random.randint(1,10) for i in range(0,100)]

punctuality=[random.randint(1,10) for i in range(0,100)]

marks=[random.randint(35,100) for i in range(0,100)]

dataframe=pd.DataFrame({'hours of study' : hours_of_study,
                        'Diversity of skills' : Diversity_of_Skills,
                        'Technical Knowledge' : Technical_knowledge,
                        'Dedication' : Dedication,
                        'Punctuality' : punctuality,
                        'Marks' : marks})

dataframe.to_csv('StudentMarks.csv')
                        
