// Modern JavaScript for Gyanam Automation Platform

// Search functionality
document.getElementById('searchInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        performSearch();
    }
});

function performSearch() {
    const searchTerm = document.getElementById('searchInput').value;
    if (searchTerm.trim()) {
        // Redirect to documentation system with search
        window.location.href = `/documentation/?search=${encodeURIComponent(searchTerm)}`;
    }
}

// Demo functions for featured workflows
function openDemo(workflowType) {
    // Map workflow types to your existing showcase pages
    const demoUrls = {
        'ama-bot': '/showcase/ama-bot.html',
        'voice-bot': '/showcase/voicebot.html',
        'whatsapp-bot': '/showcase/whatsapp-bot.html',
        'telegram-voice': '/showcase/telegram-voice.html',
        'elevenlabs': '/showcase/elevenlabs.html',
        'voiceflow': '/showcase/voiceflow.html'
    };
    
    const url = demoUrls[workflowType];
    if (url) {
        window.open(url, '_blank');
    } else {
        alert('Demo coming soon! This workflow is being prepared for demonstration.');
    }
}

// Download workflow function
function downloadWorkflow(workflowType) {
    // This would connect to your existing workflow download system
    alert(`Downloading ${workflowType} workflow... This will connect to your workflow browser.`);
    // You can implement actual download logic here
}

// Navigation functions
function openBrowser() {
    window.location.href = '/documentation/';
}

function openDocumentation() {
    window.location.href = '/documentation/';
}

function openAPI() {
    window.location.href = '/api/workflows';
}

// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Loading animation
window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});

