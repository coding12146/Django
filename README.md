# 📌 Pre-assignment: Requirements for a Task Management System

## 📍 Scenario Description
Employee Kim has joined Danbi Education and has been assigned tasks. Kim Wink must collaborate with other teams to complete these tasks. A system to create and manage tasks (Tasks) needs to be developed. The following are the system requirements. Teams Danbi, Darae, Blabla, Cheollo, Ttangi, Haetae, and Supee - a total of 7 teams - are involved. To facilitate this, Kim Wink must be able to create a task (Task) and set the teams required for collaboration as subtasks (SubTask), thereby requesting work from these teams.

## 📍 Conditions
- When creating a task, one or more teams must be set.
- However, the team creating the task (Task) does not necessarily have to be included in the subtasks (SubTask).
  - e.g., The Danbi Team, when creating a task (Task), can set Danbi, Darae, Cheollo as subteams in the subtask. However, if the Danbi team does not need to work on the task, it is not necessary to include the Danbi team in the subtask.
- Only the predefined 7 teams can be assigned as subtasks (SubTask). No other teams can be included.
- Tasks (Task) can be modified, including the teams in subtasks (SubTask), as long as the subtask is not completed.
  - e.g., If the Danbi Team sets Danbi, Darae, Cheollo as subteams and later wants to change it to Danbi only or Danbi, Darae, Supee, it can be done flexibly. If there are any completed subtasks (SubTask), they are ignored during changes.
- Tasks (Task) cannot be modified by anyone other than the author.
- Teams assigned to subtasks (SubTask) of a task (Task) should be modifiable. However, a completed subtask (SubTask) should not be deleted.

- When querying tasks (Task), if your team is included in the subtasks (SubTask), the task should be visible in the task list.
- It should be possible to check the completion status of the subtasks (SubTask) when querying tasks (Task).
- Once all subtasks (SubTask) of a task (Task) are completed, the parent task (Task) should be automatically marked as completed.
- Completion of a subtask (SubTask) can only be done by the team assigned to it.

## 📍 DB Schema
### Task
- id ()
- create_user ()
- team ()
- title ()
- content ()
- is_complete ( , default=False)
- completed_date ()
- created_at ()
- modified_at ()
### SubTask 
- id () 
- team ()
- is_complete ( , default=False) 
- completed_date ()
- created_at () 
- modified_at () 
### USER(abstract)
- id ()
- username () 
- pw ()
- team ()

## 📍 FAQ
- Can the database structure be changed?
  - Yes, you can change it to what you think is the optimal structure. However, if you change field names, they need to be understandable.
- Can I use libraries?
  - You may use libraries if you deem them necessary for the task.
- Do I need to implement sign-up and login features?
  - These are not mandatory. Implement them if you think they are necessary.

- Restrictions
  - Please implement using Python, Django, and DRF.
- Version Requirements
  - djangorestframework>3.0 
  - django>3.2
  - python>3.9
- You are free to choose the database.
- Please implement as a Restful API.
- Feel free to implement any additional APIs you think are necessary.
- Please write 'necessary' test codes.

# 📌 Key Points to Check
- Ensure the functionality works as intended.
- Check the operation of the test codes.
- Enable database query logging and check for inefficient queries.
- Review the overall project structure.
- Ensure the source code is well-organized and readable.
