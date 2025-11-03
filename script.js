const startBtn = document.getElementById('start-chat');
const chatSection = document.getElementById('chat-section');
const closeBtn = document.getElementById('close-chat');
const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chatWindow = document.getElementById('chat-window');

startBtn.addEventListener('click', () => chatSection.classList.remove('hidden'));
closeBtn.addEventListener('click', () => chatSection.classList.add('hidden'));

function appendMessage(sender, text) {
  const msg = document.createElement('div');
  msg.className = 'message ' + sender;
  msg.textContent = text;
  chatWindow.appendChild(msg);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const userMsg = input.value.trim();
  if (!userMsg) return;
  appendMessage('user', userMsg);
  input.value = '';
  appendMessage('bot', 'Carling is thinking...');

  try {
    const res = await fetch('http://127.0.0.1:5000/api/chat', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({message: userMsg, userId: 'demo123'})
    });
    const data = await res.json();
    chatWindow.lastChild.textContent = data.response || "No response available.";
  } catch {
    chatWindow.lastChild.textContent = 'Error: Unable to reach backend.';
  }
});

