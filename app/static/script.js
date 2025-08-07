const majorToCourses = JSON.parse(document.getElementById('majorToCoursesData').textContent);

function populateCourses() {
    const majorSelect = document.getElementById("major");
    const courseSelect = document.getElementById("course");

    // Clear previous options
    courseSelect.innerHTML = '<option value="">-- Select a Course --</option>';

    const selectedMajor = majorSelect.value;
    if (selectedMajor in majorToCourses) {
        majorToCourses[selectedMajor].forEach(course => {
            const option = document.createElement("option");
            option.value = course;
            option.textContent = course;
            courseSelect.appendChild(option);
        });
    }
}
