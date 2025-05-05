document.addEventListener('DOMContentLoaded', function() {
    const jobList = document.getElementById('job-list');
    const searchInput = document.getElementById('search');
    const categoryFilter = document.getElementById('category-filter');
    const applicationForm = document.getElementById('application-form');

    // Fetch job listings from the backend
    function fetchJobs() {
        fetch('/jobs')
            .then(response => response.json())
            .then(data => {
                displayJobs(data);
            });
    }

    // Display job listings
    function displayJobs(jobs) {
        jobList.innerHTML = '';
        jobs.forEach(job => {
            const li = document.createElement('li');
            li.textContent = job.title;
            jobList.appendChild(li);
        });
    }

    // Search and filter jobs
    searchInput.addEventListener('input', filterJobs);
    categoryFilter.addEventListener('change', filterJobs);

    function filterJobs() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedCategory = categoryFilter.value;

        const filteredJobs = jobListings.filter(job => {
            const matchesSearch = job.title.toLowerCase().includes(searchTerm);
            const matchesCategory = selectedCategory ? job.category === selectedCategory : true;
            return matchesSearch && matchesCategory;
        });

        displayJobs(filteredJobs);
    }

    // Handle user registration
    registrationForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const registrationData = {
            username: document.getElementById('username').value,
            password: document.getElementById('password').value,
        };

        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(registrationData),
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            registrationForm.reset();
        });
    });

    // Handle user login
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const loginData = {
            username: document.getElementById('login-username').value,
            password: document.getElementById('login-password').value,
        };

        fetch('/login', {

            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(loginData),
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            loginForm.reset();
        });
    });

    // Initial fetch of jobs

    fetchJobs();
});
