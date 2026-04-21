// Gemini Chatbot JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const chatMessages = document.getElementById('chat-messages');
    const typingIndicator = document.querySelector('.typing-indicator');

    // Send message on button click
    sendButton.addEventListener('click', sendMessage);

    // Send message on Enter key
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Auto-resize textarea
    messageInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });

    async function sendMessage() {
        const message = messageInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addMessage(message, 'user');
        messageInput.value = '';
        messageInput.style.height = 'auto';

        // Show typing indicator
        typingIndicator.classList.add('show');

        // Disable input while processing
        sendButton.disabled = true;
        messageInput.disabled = true;

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();

            if (response.ok) {
                addMessage(data.response, 'bot');
            } else {
                addMessage('Error: ' + (data.error || 'Unknown error'), 'bot');
            }
        } catch (error) {
            addMessage('Error: Could not connect to server', 'bot');
            console.error('Error:', error);
        } finally {
            // Hide typing indicator
            typingIndicator.classList.remove('show');

            // Re-enable input
            sendButton.disabled = false;
            messageInput.disabled = false;
            messageInput.focus();
        }
    }

    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;

        const textDiv = document.createElement('div');
        textDiv.textContent = text;

        const timestamp = document.createElement('div');
        timestamp.className = 'timestamp';
        timestamp.textContent = new Date().toLocaleTimeString();

        messageDiv.appendChild(textDiv);
        messageDiv.appendChild(timestamp);

        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Focus on input when page loads
    messageInput.focus();

    // Add welcome message
    setTimeout(() => {
        addMessage('Hello! I\'m your Gemini AI assistant. How can I help you today?', 'bot');
    }, 500);
});