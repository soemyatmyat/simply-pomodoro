<template>
<!-- Image and text -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
  <a class="navbar-brand" @click="handleSettings" style="cursor: pointer;" ><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-gear" viewBox="0 0 16 16">
    <path d="M8 4.754a3.246 3.246 0 1 0 0 6.492 3.246 3.246 0 0 0 0-6.492M5.754 8a2.246 2.246 0 1 1 4.492 0 2.246 2.246 0 0 1-4.492 0"/>
    <path d="M9.796 1.343c-.527-1.79-3.065-1.79-3.592 0l-.094.319a.873.873 0 0 1-1.255.52l-.292-.16c-1.64-.892-3.433.902-2.54 2.541l.159.292a.873.873 0 0 1-.52 1.255l-.319.094c-1.79.527-1.79 3.065 0 3.592l.319.094a.873.873 0 0 1 .52 1.255l-.16.292c-.892 1.64.901 3.434 2.541 2.54l.292-.159a.873.873 0 0 1 1.255.52l.094.319c.527 1.79 3.065 1.79 3.592 0l.094-.319a.873.873 0 0 1 1.255-.52l.292.16c1.64.893 3.434-.902 2.54-2.541l-.159-.292a.873.873 0 0 1 .52-1.255l.319-.094c1.79-.527 1.79-3.065 0-3.592l-.319-.094a.873.873 0 0 1-.52-1.255l.16-.292c.893-1.64-.902-3.433-2.541-2.54l-.292.159a.873.873 0 0 1-1.255-.52zm-2.633.283c.246-.835 1.428-.835 1.674 0l.094.319a1.873 1.873 0 0 0 2.693 1.115l.291-.16c.764-.415 1.6.42 1.184 1.185l-.159.292a1.873 1.873 0 0 0 1.116 2.692l.318.094c.835.246.835 1.428 0 1.674l-.319.094a1.873 1.873 0 0 0-1.115 2.693l.16.291c.415.764-.42 1.6-1.185 1.184l-.291-.159a1.873 1.873 0 0 0-2.693 1.116l-.094.318c-.246.835-1.428.835-1.674 0l-.094-.319a1.873 1.873 0 0 0-2.692-1.115l-.292.16c-.764.415-1.6-.42-1.184-1.185l.159-.291A1.873 1.873 0 0 0 1.945 8.93l-.319-.094c-.835-.246-.835-1.428 0-1.674l.319-.094A1.873 1.873 0 0 0 3.06 4.377l-.16-.292c-.415-.764.42-1.6 1.185-1.184l.292.159a1.873 1.873 0 0 0 2.692-1.115z"/>
  </svg></a>Simply Pomodoro | LinkedIn | GitHub | Personal Blog
  </div>
</nav>
  <div class="container">
    <div class="row">
        <div class="col-md-6 offset-md-3">
          <h3 style="text-align: center;">{{ selectedTask !== null ? selectedTask.name : 'Choose a task' }} <svg @click="stopTimer" style="cursor: pointer;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-clockwise" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 1 .908-.417A6 6 0 1 1 8 2z"/>
            <path d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 4.658A.25.25 0 0 1 8 4.466"/>
          </svg></h3>
          <div class="circle">
            <svg width="300" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">
              <g transform="translate(110,110)">
                 <circle r="100" class="e-c-base"/>
                 <g transform="rotate(-90)">
                    <circle r="100" class="e-c-progress" :style="{ strokeDasharray: circumference, strokeDashoffset: dashoffset, stroke: strokecolor }"/>
                    <g id="e-pointer" :style="{ transform: `rotate(${rotation}deg)` }">
                       <circle cx="100" cy="0" r="8" class="e-c-pointer" :style="{ stroke: strokecolor }"/>
                    </g>
                 </g>
                 <text x="0" y="5" font-size="40" text-anchor="middle" :style="{fill: strokecolor}">{{ formatTime(minutes) }}:{{ formatTime(seconds) }}</text>
                
                 <text x="0" y="60" font-size="16" text-anchor="middle" @click="handleAction" :style="{cursor:'pointer', fill:strokecolor }">{{ action }}</text>

              </g>
           </svg>
          </div>
        </div>
    </div>
    <div class="row">
        <button type="button" class="btn btn-outline-success btn-sm" @click="toggleAddTaskModal">Add a New Task </button>
        <br><br><br><br>
        <table class="table table-responsive ">
          <thead>
              <tr>
              <th scope="col">Name</th>
              <th scope="col">Pomodoro</th>
              <th scope="col">Minutes</th>
              <th scope="col">Status</th>
              <th></th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="(task, index) in tasks" :key="index">
                <td><input class="form-check-input" type="radio" v-model="selectedTask" :value="task" :disabled="task.status == 'Completed' || timerRunning" name="rowSelection"> {{ task.name }}</td>
                <td>
                  <span v-for="n in task.completed" class="dot-filled"></span>
                  <span v-for="n in task.pomodoro" class="dot"></span>
                </td>
                <td>{{task.completed * 25}} / {{ (task.pomodoro + task.completed) * 25}}</td>
                <td>{{ task.status }}</td>
                <td>
                    <div class="btn-group" role="group">
                      <button v-if="task.status != 'Completed'" type="button" class="btn btn-warning btn-sm" @click="toggleEditTaskModal(task)" :disabled="task == selectedTask"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pen" viewBox="0 0 16 16">
                        <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001m-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708z"/>
                      </svg></button>
                      <button type="button" class="btn btn-danger btn-sm" @click="handleDeleteTask(task)" :disabled="task == selectedTask"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
                        <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
                      </svg></button>
                    </div>
                </td>
              </tr>
          </tbody>
        </table>
    </div>

    <!-- add new modal -->
    <div ref="addTaskModal" class="modal fade" :class="{ show: activeAddTaskModal, 'd-block': activeAddTaskModal }" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new task </h5>
            <button type="button" class="btn-close btn-close" data-dismiss="modal" aria-label="Close" @click="toggleAddTaskModal"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addName" class="form-label">Name:</label>
                <input ref="name" type="text" class="form-control" id="addName" v-model="addTaskForm.name" placeholder="Name" maxlength="50" required>
              </div>
              <div class="mb-3">
                <label for="addPomodoro" class="form-label">Pomodoro:</label>
                <input type="number" class="form-control" id="addPomodoro" v-model="addTaskForm.pomodoro" placeholder="3" :min="1" :max="10" required>
              </div>
              <div class="btn-group" role="group">
                <button type="submit" class="btn btn-primary btn-sm" @click="handleAddSubmit"> Submit</button>
                <button type="button" class="btn btn-danger btn-sm" @click="handleAddReset"> Reset </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddTaskModal" class="modal-backdrop fade show"></div>

    <!-- edit task modal -->
    <div ref="editTaskModal" class="modal fade" :class="{ show: activeEditTaskModal, 'd-block': activeEditTaskModal }" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Update</h5>
            <button type="button" class="btn-close btn-close" data-dismiss="modal" aria-label="Close" @click="toggleEditTaskModal"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="editTaskName" class="form-label">Name:</label>
                <input ref="editname" type="text" class="form-control" id="editTaskName" v-model="editTaskForm.name" placeholder="name" maxlength="50" required>
              </div>
              <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="editStatus" v-model="editTaskForm.complete">
                <label class="form-check-label" for="editStatus">Completed?</label>
              </div>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-primary btn-sm" @click="handleEditSubmit"> Submit </button>
                <button type="button" class="btn btn-danger btn-sm" @click="handleEditCancel"> Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeEditTaskModal" class="modal-backdrop fade show"></div>


    <!-- Settings -->
    <div class="modal fade" :class="{ show: activeSettingsModal, 'd-block': activeSettingsModal }" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Settings</h5>
            <button type="button" class="btn-close btn-close" data-dismiss="modal" aria-label="Close" @click="toggleSettingsModal"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="" class="form-label">Pomodoro Time (minutes):</label>
                <!-- <input type="integer" class="form-control" id="pomodotime" v-model="settings.pomodotime" placeholder="25" min="10" max="60" value="25"> -->
                <input type="number" class="form-control" v-model="settings.pomodotime" :min="5" :max="60" step="5">
              </div>
              <div class="mb-3">
                <label for="" class="form-label">Short Break (minutes):</label>
                <input type="number" class="form-control" id="shortbreak" v-model="settings.shortbreak" placeholder="5" min="5" max="60" value="5" step="5">
              </div>
              <div class="mb-3">
                <label for="" class="form-label">Long Break (minutes):</label>
                <input type="number" class="form-control" id="longbreak" v-model="settings.longbreak" placeholder="5" min="5" max="60" value="5" step="5">
              </div>
              <div class="mb-3 form-check form-switch">
                <label for="" class="form-label">Music</label>
                <input class="form-check-input" type="checkbox" v-model="settings.music" role="switch" id="music" checked>
              </div>
              <div class="mb-3 form-check form-switch">
                <label for="" class="form-label">Notification</label>
                <input class="form-check-input" type="checkbox" v-model="settings.notification" role="switch" id="notification">
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeSettingsModal" class="modal-backdrop fade show"></div>

  </div>
</template>

  <script>
    import axios from 'axios';
    axios.defaults.baseURL = 'http://127.0.0.1:5000';
    //axios.defaults.withCredentials = true;
    axios.defaults.crossDomain = true;
    export default {
      data() {
        return {
          timerRunning: false,
          minutes: 0,
          seconds: 10,
          circumference: 2 * Math.PI * 100,
          timerInterval: null,
          activeAddTaskModal: false,
          activeEditTaskModal: false,
          activeSettingsModal: false,
          selectedTask: null,
          dashoffset: '',
          rotation: '',
          action: 'Play',
          mode: 'Focus',
          strokecolor: '#51B170', //6085C5-51B170
          session_id: '',
          addTaskForm: {
            name: '',
            pomodoro: 3,
          },
          tasks: [],
          editTaskForm: {
            id: '',
            name: '',
            pomodoro: '',
            status: [],
          },
          settings: {
            shortbreak: 1,
            longbreak: 1,
            pomodotime: 1,
            music: true,
            notification: false,
            count: 0,
          },
        };
      },
      methods: {
        handleAction() {
          if (this.action === 'Play' && this.selectedTask != null && this.selectedTask.status != 'Completed') {
            this.startTimer();
          } else if (this.action === 'Pause') {
            this.pauseTimer();
          } else {
            alert("Please select a task to pomodoro.");
          }
        },
        formatTime(value) {
          // Format time values to add leading zeros if needed
          return value < 10 ? `0${value}` : value;
        },
        startTimer() {
          if (!this.timerRunning) {
            this.timerInterval = setInterval(this.tick, 1000);
            this.timerRunning = true;
            this.action = 'Pause';
          }
        },
        pauseTimer() {
          clearInterval(this.timerInterval);
          this.timerRunning = false;
          this.action = 'Play';
        },
        stopTimer() {
          clearInterval(this.timerInterval);
          this.timerRunning = false;
          this.action = 'Play';
          this.count = this.mode === 'Focus' ? this.count++: this.count;
          this.resetTimer();
        },
        tick() {
          if (this.seconds > 0) {
            this.seconds--;
          } else if (this.minutes > 0) {
            this.minutes--;
            this.seconds = 59;
          } else {
            if (this.mode === 'Focus') {
              const status = this.selectedTask.pomodoro === 1 ? 'Completed' : 'In Progress';
              const payload = {
                name: this.selectedTask.name,
                pomodoro: this.selectedTask.pomodoro - 1,
                completed: this.selectedTask.completed + 1,
                status: status
              };
              this.updateTask(payload, this.selectedTask.id);
            }
            // Timer reached zero, stop the timer
            this.stopTimer();
          }
          document.title = this.mode + " | " +  this.formatTime(this.minutes) + ":" + this.formatTime(this.seconds);
        },
        resetTimer() { // call from stoptimer, closeSettings

          if (this.minutes == 0 && this.selectedTask.pomodoro != 0) { // toggle between Focus/Break
            this.mode = this.mode === 'Focus' ? 'Break': 'Focus';
          }
          this.minutes = this.mode === 'Focus' ? this.settings.pomodotime: this.settings.shortbreak;
          this.strokecolor = this.mode === 'Focus' ? '#51B170': '#6085C5';
          if (this.count == 4 && this.mode === 'Break') { // every 4 pomodoro, take a long break
            this.minutes = this.settings.longbreak;
            this.count = 0; // reset count
          }
          this.seconds = 0;
          
          // if (this.selectedTask != null) { 
          //   alert(String(this.selectedTask.pomodoro));
          //   if (this.minutes == 0 && this.selectedTask.pomodoro != 0) { // toggle between Focus/Break
          //     this.mode = this.mode === 'Focus' ? 'Break': 'Focus';
          //   }
          //   this.strokecolor = this.mode === 'Focus' ? '#51B170': '#6085C5';

          //   if (this.count == 4 && this.mode === 'Break') { // every 4 pomodoro, take a long break
          //     this.minutes = this.settings.longbreak;
          //     this.count = 0; // reset count
          //   }
          //   this.seconds = 0;
          // }
          
        },
        updateSettings() {
          this.selectedTask = null;
          this.mode == 'Focus';
          this.mintues = this.settings.pomodotime;
        },
        updateDasharray() { // handle trickle down effect
          const totalDuration = this.mode === 'Focus' ? this.settings.pomodotime * 60: this.settings.shortbreak * 60;
          const remainingTime = this.minutes * 60 + this.seconds;
          const timePercent = 1-(remainingTime / totalDuration);
          this.dashoffset = this.circumference * timePercent;
          this.rotation = -360 * timePercent;
        },
        addTask(payload) {
          axios.post('/tasks', payload, {headers: {'X-Session-ID': localStorage.getItem('session_id')}})
            .then(() => {
              this.getTasks();
            })
            .catch((error) => {
              console.log(error);
              this.getTasks();
            });
        },
        updateTask(payload, taskId) {
          const path = `/tasks/${taskId}`;
          axios.put(path, payload, {headers: {'X-Session-ID': localStorage.getItem('session_id')}})
            .then(() => {
              this.getTasks();
              //this.selectedTask = res.data.task;
            })
            .catch((error) => {
              console.error(error);
              this.getTasks();
            });
        },
        removeTask(taskId) {
          const path = `/tasks/${taskId}`;
          axios.delete(path, {headers: {'X-Session-ID': localStorage.getItem('session_id')}})
            .then(() => {
              this.getTasks();
            })
            .catch((error) => {
              console.error(error);
              this.getTasks();
            })
        },
        getTasks() {
          /// neeed to retrieve session id from cookie 
          //this.session_id = sessionStorage.getItem('session_id');
          //alert(localStorage.getItem('session_id'));
          axios.get('/tasks', { headers: {'X-Session-ID': localStorage.getItem('session_id')} })
            .then((res) => {
              this.tasks = res.data.tasks;
              if (res.data.session_id) {
                //this.session_id = res.data.session_id;
                //document.cookies = `session_id=${res.data.session_id}; path=/`;
                localStorage.setItem('session_id', res.data.session_id);
              }
            })
            .catch((error) => {
              console.error(error);
            });
        },
        handleAddReset() {
          this.initForm();
        },
        handleAddSubmit() {
          if (this.addTaskForm.name.trim() != '') {
            this.toggleAddTaskModal();
            const payload = {
              name: this.addTaskForm.name,
              pomodoro: this.addTaskForm.pomodoro
            };
            this.addTask(payload);
            this.initForm();
          }
        },
        handleEditSubmit() {
          this.toggleEditTaskModal(null);
          this.editTaskForm.complete ? status="Completed": status=editTaskForm.status;
          const payload = {
            name: this.editTaskForm.name,
            pomodoro: this.editTaskForm.pomodoro,
            completed: this.editTaskForm.completed,
            status: status
          };
          this.updateTask(payload, this.editTaskForm.id);
        },
        handleEditCancel() {
          this.toggleEditTaskModal(null);
        },
        handleDeleteTask(task) {
          this.removeTask(task.id);
        },
        initForm() {
          this.addTaskForm.name = '';
          this.addTaskForm.pomodoro = 3;
        },
        toggleAddTaskModal() {
          const body = document.querySelector('body');
          this.activeAddTaskModal = !this.activeAddTaskModal;
          if (this.activeAddTaskModal) {
            body.classList.add('modal-open');
            this.$nextTick(() => {
              this.$refs.name.focus();
            });
          } else {
            body.classList.remove('modal-open');
          }
        },
        toggleEditTaskModal(task) {
          if (task) {
            this.editTaskForm = task;
          }
          const body = document.querySelector('body');
          this.activeEditTaskModal = !this.activeEditTaskModal;
          if (this.activeEditTaskModal) {
            body.classList.add('modal-open');
            this.$nextTick(() => {
              this.$refs.editname.focus();
            });
          } else {
            body.classList.remove('modal-open');
          }
        },
        handleSettings() {
          this.toggleSettingsModal();
        },
        toggleSettingsModal() {
          const body = document.querySelector('body');
          this.activeSettingsModal = !this.activeSettingsModal;
          if (this.activeSettingsModal) {
            body.classList.add('modal-open');
          } else {
            body.classList.remove('modal-open');
            this.updateSettings();
          }
        },
      },
      watch: {
          // Watch for changes in minutes and seconds and update dasharray
          minutes: 'updateDasharray',
          seconds: 'updateDasharray',
      },
      created() {
        this.getTasks();
      },
    };
  </script>
