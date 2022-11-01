baseRadius = 6
midRadius = 4
topRadius = 2

cmds.polySphere( n='base', sx=10, sy=10, r=baseRadius)
cmds.move (0, 6, 0, 'base', worldSpace=True)

cmds.polySphere (n='mid', sx = 10, sy = 10, r = midRadius)
cmds.move (0, ((baseRadius * 2) + midRadius), 0, 'mid', worldSpace = True)

cmds.polySphere (n='top', sx = 10, sy = 10, r = topRadius)
cmds.move (0, ((baseRadius * 2) + (midRadius * 2) + topRadius), 0, 'top', worldSpace = True)

cmds.group( 'base', 'mid', 'top', name = 'BodyGeo_Grp')
