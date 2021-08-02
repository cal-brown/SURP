\ Model RAP
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  2 assign[1,0,0] + 5 assign[2,0,0] + 3 assign[3,0,0] + 1.5 assign[1,0,1]
   + 3.75 assign[2,0,1] + 2.25 assign[3,0,1]
Subject To
 supply: assign[1,0,0] + assign[2,0,0] + assign[3,0,0] + assign[1,0,1]
   + assign[2,0,1] + assign[3,0,1] <= 3
 vaccine[1]: assign[1,0,0] + assign[1,0,1] <= 1
 vaccine[2]: assign[2,0,0] + assign[2,0,1] <= 1
 vaccine[3]: assign[3,0,0] + assign[3,0,1] <= 1
 center_capacity[0,0]: assign[1,0,0] + assign[2,0,0] + assign[3,0,0] <= 2
 center_capacity[0,1]: assign[1,0,1] + assign[2,0,1] + assign[3,0,1] <= 2
Bounds
Binaries
 assign[1,0,0] assign[2,0,0] assign[3,0,0] assign[1,0,1] assign[2,0,1]
 assign[3,0,1]
End
