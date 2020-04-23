# Todos DDD Example
An example todos app with DDD approach

# Domain Modeling Iteration

## Round 1

### User stories
- User will be logged in by providing a username (no need password, no need to register)
- User could manage one ore more todo task items
- Each task's state could be as follow: new -> doing -> done
- To stay focused, user could only have 3 doing tasks at a time. But if he has finished at least 3 tasks in his lifetime usage, he could have up to 5 concurrent doing tasks
- User could delete/remove any task in the list
- No need to manage task creation time

### Domain model
![](https://www.plantuml.com/plantuml/img/VP5BJq8n48NtyoicTmM9tk3M48FH3GkC2RecG-y83UtKj7CZ-FZljlK5aT3Td7Fcv6ixIKfHU-y0qiRACqNoQ1obTAqQxR9NdfeWS_lAE0Ae3ZucZlW6cCyyXsI5VLQ4F5TjAeeQbDoY2zbSAANDFqFuI__uANt8qs6fxVQdZfFPdpEuSbcteXoVo72jc97GYZsBtWTdpUwxSXc2Gt8klDpnLcyBLqaF2lZm3s96sviWfe-HnUn-OmTLzHRho6aTN5TMwtCq5msUOpDgMsago2NwYfBm2WObSbRb8OxRzYWfm57-yNlEd-G2cB1q-Gy_0G00)
