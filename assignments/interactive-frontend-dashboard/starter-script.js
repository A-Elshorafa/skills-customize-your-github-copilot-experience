const form = document.getElementById("assignment-form");
const titleInput = document.getElementById("assignment-title");
const courseInput = document.getElementById("assignment-course");
const list = document.getElementById("assignment-list");
const filterButtons = document.querySelectorAll(".filter-btn");

const assignments = [];
let currentFilter = "all";

function renderAssignments() {
  list.innerHTML = "";

  const filtered = assignments.filter((item) => {
    if (currentFilter === "active") return !item.completed;
    if (currentFilter === "completed") return item.completed;
    return true;
  });

  filtered.forEach((item) => {
    const li = document.createElement("li");
    li.className = `assignment-card${item.completed ? " done" : ""}`;

    const info = document.createElement("div");
    info.innerHTML = `<div class="title">${item.title}</div><div class="meta">${item.course}</div>`;

    const toggleBtn = document.createElement("button");
    toggleBtn.textContent = item.completed ? "Undo" : "Complete";
    toggleBtn.addEventListener("click", () => {
      item.completed = !item.completed;
      renderAssignments();
    });

    li.appendChild(info);
    li.appendChild(toggleBtn);
    list.appendChild(li);
  });
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  assignments.push({
    title: titleInput.value.trim(),
    course: courseInput.value.trim(),
    completed: false,
  });

  form.reset();
  renderAssignments();
});

filterButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    currentFilter = btn.dataset.filter;
    filterButtons.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    renderAssignments();
  });
});

renderAssignments();
