/**
 * Session 4 teaching snapshot — Session 3 + mood + streak.
 * Aligns with ../../js/app.js Session 4. Validation helpers come in Session 5.
 */

const STORAGE_KEY = "sFactorPlanner";
const ALLOWED_MOODS = ["focused", "tired", "stressed", "motivated", "calm"];
let flashMessages = [];

function defaultPlannerData() {
  return {
    planner_title: "My Study Planner",
    notes: "",
    tasks: [],
    next_task_id: 1,
    mood_today: "",
    streak_days: 0,
    last_streak_date: "",
  };
}

function todayIso() {
  return new Date().toISOString().slice(0, 10);
}

function loadPlanner() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) {
    const data = defaultPlannerData();
    savePlanner(data);
    return data;
  }
  const data = JSON.parse(raw);
  const base = defaultPlannerData();
  for (const key of Object.keys(base)) {
    if (data[key] === undefined) {
      data[key] = base[key];
    }
  }
  return data;
}

function savePlanner(data) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}

function findTask(data, taskId) {
  for (const task of data.tasks) {
    if (task.id === taskId) {
      return task;
    }
  }
  return null;
}

function addTask(data, title) {
  data.tasks.push({
    id: data.next_task_id,
    title,
    done: false,
    created: todayIso(),
  });
  data.next_task_id += 1;
}

function updateStudyStreak(data) {
  const today = todayIso();
  const last = data.last_streak_date || "";
  if (last === today) {
    return;
  }
  if (last === "") {
    data.streak_days = 1;
  } else {
    const lastDay = new Date(last + "T12:00:00");
    const todayDay = new Date(today + "T12:00:00");
    const gap = Math.round((todayDay - lastDay) / (1000 * 60 * 60 * 24));
    if (gap === 1) {
      data.streak_days = Number(data.streak_days || 0) + 1;
    } else if (gap > 1) {
      data.streak_days = 1;
    } else {
      data.streak_days = Math.max(Number(data.streak_days || 0), 1);
    }
  }
  data.last_streak_date = today;
}

function completeTask(data, taskId) {
  const task = findTask(data, taskId);
  if (!task) {
    return false;
  }
  if (!task.done) {
    task.done = true;
    updateStudyStreak(data);
  }
  return true;
}

function streakMessage(streakDays) {
  if (streakDays <= 0) {
    return "Complete a task today to start your streak.";
  }
  if (streakDays === 1) {
    return "Day 1 — nice start. Keep showing up.";
  }
  return `${streakDays}-day streak! You are building a real habit.`;
}

function activeTasks(data) {
  const open = [];
  for (const task of data.tasks) {
    if (!task.done) {
      open.push(task);
    }
  }
  return open;
}

function completedTasks(data) {
  const done = [];
  for (const task of data.tasks) {
    if (task.done) {
      done.push(task);
    }
  }
  return done;
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

function showFlash(messages) {
  const list = document.getElementById("flash-list");
  list.innerHTML = "";
  if (!messages.length) {
    list.hidden = true;
    return;
  }
  for (const msg of messages) {
    const li = document.createElement("li");
    li.className = `flash flash-${msg.type === "error" ? "error" : "success"}`;
    li.textContent = msg.text;
    list.appendChild(li);
  }
  list.hidden = false;
}

function renderTaskList(listEl, tasks, mode) {
  listEl.innerHTML = "";
  for (const task of tasks) {
    const li = document.createElement("li");
    li.className = "task-card" + (mode === "done" ? " done" : "");
    const titleSpan = document.createElement("span");
    titleSpan.className = "task-title";
    titleSpan.textContent = task.title;
    li.appendChild(titleSpan);
    if (mode === "active") {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "btn btn-small";
      btn.textContent = "Complete";
      btn.dataset.taskId = String(task.id);
      btn.addEventListener("click", onCompleteTaskClick);
      li.appendChild(btn);
    } else {
      const badge = document.createElement("span");
      badge.className = "badge";
      badge.textContent = "✓";
      li.appendChild(badge);
    }
    listEl.appendChild(li);
  }
}

function render(data) {
  document.getElementById("planner-title-heading").textContent = data.planner_title;
  document.getElementById("planner_title").value = data.planner_title;
  document.getElementById("notes").value = data.notes;
  document.getElementById("mood").value = data.mood_today || "";

  const active = activeTasks(data);
  const done = completedTasks(data);
  document.getElementById("active-count").textContent = String(active.length);
  document.getElementById("done-count").textContent = String(done.length);
  renderTaskList(document.getElementById("active-tasks"), active, "active");
  renderTaskList(document.getElementById("done-tasks"), done, "done");
  document.getElementById("active-empty").hidden = active.length > 0;
  document.getElementById("done-empty").hidden = done.length > 0;

  const streakDays = Number(data.streak_days || 0);
  document.getElementById("streak-number").textContent =
    streakDays + " day" + (streakDays === 1 ? "" : "s");
  document.getElementById("streak-copy").textContent = streakMessage(streakDays);

  const moodCurrent = document.getElementById("mood-current");
  if (data.mood_today) {
    moodCurrent.hidden = false;
    moodCurrent.innerHTML = `Logged today: <strong>${escapeHtml(data.mood_today)}</strong>`;
  } else {
    moodCurrent.hidden = true;
  }

  showFlash(flashMessages);
  flashMessages = [];
}

function onCompleteTaskClick(event) {
  const data = loadPlanner();
  const taskId = Number(event.currentTarget.dataset.taskId);
  if (!Number.isInteger(taskId) || !completeTask(data, taskId)) {
    flashMessages.push({ type: "error", text: "That task no longer exists." });
    render(data);
    return;
  }
  savePlanner(data);
  flashMessages.push({ type: "success", text: "Task completed — streak updated." });
  render(loadPlanner());
}

function wireForms() {
  document.getElementById("title-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const data = loadPlanner();
    const title = document.getElementById("planner_title").value.trim();
    if (!title) {
      flashMessages.push({ type: "error", text: "Planner title cannot be empty." });
      render(data);
      return;
    }
    data.planner_title = title;
    savePlanner(data);
    flashMessages.push({ type: "success", text: "Planner title updated." });
    render(loadPlanner());
  });

  document.getElementById("task-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const data = loadPlanner();
    const input = document.getElementById("task_title");
    const title = input.value.trim();
    if (!title) {
      flashMessages.push({ type: "error", text: "Task title cannot be empty." });
      render(data);
      return;
    }
    addTask(data, title);
    savePlanner(data);
    input.value = "";
    flashMessages.push({ type: "success", text: "Task added." });
    render(loadPlanner());
  });

  document.getElementById("notes-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const data = loadPlanner();
    data.notes = document.getElementById("notes").value.trim();
    savePlanner(data);
    flashMessages.push({ type: "success", text: "Notes saved." });
    render(loadPlanner());
  });

  document.getElementById("mood-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const data = loadPlanner();
    const mood = document.getElementById("mood").value.trim().toLowerCase();
    if (mood && !ALLOWED_MOODS.includes(mood)) {
      flashMessages.push({ type: "error", text: "Please pick a mood from the list." });
      render(data);
      return;
    }
    data.mood_today = mood;
    savePlanner(data);
    flashMessages.push({
      type: "success",
      text: mood ? `Mood logged: ${mood}.` : "Mood cleared.",
    });
    render(loadPlanner());
  });
}

document.addEventListener("DOMContentLoaded", () => {
  wireForms();
  render(loadPlanner());
});
