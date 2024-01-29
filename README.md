## Description
A simple intuitive single page pomodoro application with progress web app features. 
Download-able, Install-able as an app to mobile devices. Works with or without internet!

###  Iteration 0.1 
[done] Flask Boiler-plate
[done] VUE Boiler-plate
[done] CRUD Task
[done] Timer Play, Pause, Reset
[done] Display Running Task + Update Pomodoro of Running Task 
[done] Auto-switch between Focus and Break 
[done] UI aesthetic (dark, light, auto mode, color schemes)

### Iteration 0.2 
[done] Service Worker + mainfest
[done] Push Notification API
[done] Settings (Pomodo, Short Break, Long Break, Auto-continue, Music, Notifications) 
[done] Enablement of Long Break
[ ] Add Background music (Rain Piano Cafe on loop)
[done] UI Validation + Intuitive Check
[done] Storing session_id in Local Storage (users do not need to login => limit one session to 10 tasks max.)
[done] Data Storage for offline capability 
    |-- [done] Cache Storage API: network resources 
    |-- [done] IndexedDB (NoSQL, Object-oriented): structured data (at the end of the session, the data is wiped out.)
    |-- [done] Local Storage: session_id (only when online)

### Iteration 0.3 ** 
[done] Hosting consideration 
[ ] Fix Notificatin in Production 
[ ] Login Module (with Database)
 |-- [ ] No limit of tasks when login
 |-- [ ] SW to sync with backends once online 
 |-- [ ] Handle uuid hex 
 
### Iteration 0.4 **
[ ] Data Analytics for registered users only
[ ] Data Analytics with Import/Export Capability 


## References
Notification API: https://developer.mozilla.org/en-US/docs/Web/API/Notification
IndexedDB API: https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API

## Credits:
Favicon from <a href="https://www.flaticon.com/free-icons/pomodoro" title="pomodoro icons">Pomodoro icons created by nangicon - Flaticon</a>
