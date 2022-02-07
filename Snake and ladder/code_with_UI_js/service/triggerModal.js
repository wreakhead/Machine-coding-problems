export const triggerModal = (message) => {
  document.getElementById("moveInfo").innerHTML = "";
  document.getElementById("moveInfo").innerHTML += message;
  document.getElementById("triggerModalBtn").click();
};
