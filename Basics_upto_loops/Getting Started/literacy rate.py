'''to find the total number of illiterate men and women
if the population of the town is 80,000'''

__author__ = "Shakir Sadiq"

Total_Population = 80000 #totalpopulation
Population_Men = (52*Total_Population)/100 #menpopulation
Population_Women = (Total_Population - Population_Men) #womenpopulation
Total_Literacy = (48*Total_Population)/100 #literacy
Literate_Men = (35*Total_Population)/100 #literatemen
Literate_Women = (Total_Literacy - Literate_Men) #literatewomen
Illiterate_men = (Population_Men - Literate_Men) #illiteratemen
Illiterate_Women = (Population_Women - Literate_Women) #illiteratewomen
print('Total population=',Total_Population)
print('Total number of illiterate men= ',Illiterate_men)
print('Total number of illiterate women= ',Illiterate_Women)
