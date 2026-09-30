// Session 1: prove the script runs after the HTML is ready.
document.addEventListener("DOMContentLoaded", () => {
  const heading = document.getElementById("welcome");
  if (heading) {
    heading.textContent = "My Study Planner is live!";
  }
});
