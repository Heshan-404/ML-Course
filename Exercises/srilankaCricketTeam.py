oldTeam = {'mahela','murali','chandi','mathews'}
newTeam = {'medis','mathews','sangakkar','chandi','dimuth'}

print(f"2015 old wc squad is :  {oldTeam}\n" )
print(f"2019 wc squad is :  {newTeam}\n" )

print(f"Expirenced players : {oldTeam & newTeam}\n")

print(f"New playes in 2019 : {newTeam - oldTeam}\n" )

print(f"Retied players : {oldTeam - newTeam}\n" )

print(f"{oldTeam | newTeam}\n")