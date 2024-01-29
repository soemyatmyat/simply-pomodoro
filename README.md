## Description
A simple intuitive single page pomodoro application with progress web app features. 
Download-able, Install-able as an app to mobile devices. Works with or without internet!

###  Iteration 0.1 
- [x] Flask Boiler-plate
- [x] VUE Boiler-plate
- [x] CRUD Task
- [x] Timer Play, Pause, Reset
- [x] Display Running Task + Update Pomodoro of Running Task 
- [x] Auto-switch between Focus and Break 
- [x] UI aesthetic (dark, light, auto mode, color schemes)

### Iteration 0.2 
- [x] Service Worker + mainfest
- [x] Push Notification API
- [x] Settings (Pomodo, Short Break, Long Break, Auto-continue, Music, Notifications) 
- [x] Enablement of Long Break
- [ ] Add Background music (Rain Piano Cafe on loop)
- [x] UI Validation + Intuitive Check
- [x] Storing session_id in Local Storage (users do not need to login => limit one session to 10 tasks max.)
- [x] Data Storage for offline capability 
- - [x] Cache Storage API: network resources 
- - [x] IndexedDB (NoSQL, Object-oriented): structured data (at the end of the session, the data is wiped out.)
- - [x] Local Storage: session_id (only when online)

### Iteration 0.3
- [x] Hosting consideration 
- [ ] Fix Notificatin in Production 
- [ ] Add Background music (Rain Piano Cafe on loop)
- [ ] Revist UI aesthetic 
- [ ] Login Module (with Database)
- - [ ] No limit of tasks when login
- - [ ] SW to sync with backends once online 
- - [ ] Handle uuid hex 
 
### Iteration 0.4
- [ ] Data Analytics for registered users only
- [ ] Data Analytics with Import/Export Capability 


## References
- Notification API: https://developer.mozilla.org/en-US/docs/Web/API/Notification
- IndexedDB API: https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API

## Credits:
- Favicon from <a href="https://www.flaticon.com/free-icons/pomodoro" title="pomodoro icons">Pomodoro icons created by nangicon - Flaticon</a>
