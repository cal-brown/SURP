\ Model RAP
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  7 assign[1,0,0] + 5 assign[2,0,0] + 3 assign[3,0,0] + assign[4,0,0]
   + 7 assign[1,1,0] + 5 assign[2,1,0] + 3 assign[3,1,0] + assign[4,1,0]
   + 5.25 assign[1,0,1] + 3.75 assign[2,0,1] + 2.25 assign[3,0,1]
   + 0.75 assign[4,0,1] + 5.25 assign[1,1,1] + 3.75 assign[2,1,1]
   + 2.25 assign[3,1,1] + 0.75 assign[4,1,1]
Subject To
 supply: assign[1,0,0] + assign[2,0,0] + assign[3,0,0] + assign[4,0,0]
   + assign[1,1,0] + assign[2,1,0] + assign[3,1,0] + assign[4,1,0]
   + assign[1,0,1] + assign[2,0,1] + assign[3,0,1] + assign[4,0,1]
   + assign[1,1,1] + assign[2,1,1] + assign[3,1,1] + assign[4,1,1] <= 3
 vaccine[1]: assign[1,0,0] + assign[1,1,0] + assign[1,0,1] + assign[1,1,1]
   <= 1
 vaccine[2]: assign[2,0,0] + assign[2,1,0] + assign[2,0,1] + assign[2,1,1]
   <= 1
 vaccine[3]: assign[3,0,0] + assign[3,1,0] + assign[3,0,1] + assign[3,1,1]
   <= 1
 vaccine[4]: assign[4,0,0] + assign[4,1,0] + assign[4,0,1] + assign[4,1,1]
   <= 1
 center_capacity[0,0]: assign[1,0,0] + assign[2,0,0] + assign[3,0,0]
   + assign[4,0,0] <= 1
 center_capacity[0,1]: assign[1,0,1] + assign[2,0,1] + assign[3,0,1]
   + assign[4,0,1] <= 1
 center_capacity[1,0]: assign[1,1,0] + assign[2,1,0] + assign[3,1,0]
   + assign[4,1,0] <= 1
 center_capacity[1,1]: assign[1,1,1] + assign[2,1,1] + assign[3,1,1]
   + assign[4,1,1] <= 1
Bounds
Binaries
 assign[1,0,0] assign[2,0,0] assign[3,0,0] assign[4,0,0] assign[1,1,0]
 assign[2,1,0] assign[3,1,0] assign[4,1,0] assign[1,0,1] assign[2,0,1]
 assign[3,0,1] assign[4,0,1] assign[1,1,1] assign[2,1,1] assign[3,1,1]
 assign[4,1,1]
End
