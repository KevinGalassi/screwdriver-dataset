
# Dataset Content Organization


ok : Screwdriver succefully manage to activate and conclude the screw. \
misfire : Error in the screwdriver control. \
fail: Screwdriver activate, but failed in the screwdriver. \


```
dataset
   │
   └───screwing
   │   │
   │   └───fail
   |   |   └─── force
   |   |   └─── position
   │   └───misfire
   |   |   └─── force
   |   |   └─── position
   │   └───ok
   |       └─── force
   |       └─── position
   │   
   └───unscrewing
      └─── fail
      └─── misfire
      └─── ok
```