const links = document.querySelectorAll('.nav-link');
links.forEach(link => {
  link.addEventListener('click', smoothScroll);
});

function smoothScroll(e) {
  e.preventDefault();
  const targetId = this.getAttribute('href');
  const targetPosition = document.querySelector(targetId).offsetTop;
  window.scrollTo({
    top: targetPosition,
    behavior: 'smooth'
  });
}

/* Highlight active link on scroll */
window.addEventListener('scroll', highlightActiveLink);

function highlightActiveLink() {
  let fromTop = window.scrollY + 80;

  links.forEach(link => {
    let section = document.querySelector(link.hash);

    if (
      section.offsetTop <= fromTop &&
      section.offsetTop + section.offsetHeight > fromTop
    ) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

/* Chart.js initialization */
const utilizationCtx = document.getElementById('utilizationChart').getContext('2d');
const utilizationChart = new Chart(utilizationCtx, {
  type: 'bar',
  data: {
    labels: ['January', 'February', 'March', 'April', 'May', 'June'],
    datasets: [{
      label: 'Utilization Rate',
      data: [65, 59, 80, 81, 56, 55],
      backgroundColor: '#26d9e0',
      borderColor: '#26d9e0',
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});

const maintenanceCtx = document.getElementById('maintenanceChart').getContext('2d');
const maintenanceChart = new Chart(maintenanceCtx, {
  type: 'line',
  data: {
    labels: ['January', 'February', 'March', 'April', 'May', 'June'],
    datasets: [{
      label: 'Maintenance Predictions',
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: 'rgba(38, 217, 224, 0.2)',
      borderColor: '#26d9e' ,
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});

/* Form submission handling */
document.addEventListener('DOMContentLoaded', () => {
  const addAssetButton = document.getElementById('addAssetButton');
  if (addAssetButton) {
    addAssetButton.addEventListener('click', addAsset);
  }
});

function addAsset() {
  const assetId = document.getElementById('assetId').value;
  const assetType = document.getElementById('assetType').value;
  const status = document.getElementById('status').value;
  const location = document.getElementById('location').value;

  // Example: Validate form fields (add more validation as needed)
  if (!assetId || !assetType || !status || !location) {
    alert('Please fill out all fields.');
    return;
  }

  // Example: Prepare data to send to backend (replace with actual AJAX call)
  const assetData = {
    assetId: assetId,
    assetType: assetType,
    status: status,
    location: location
  };

  // Example: AJAX POST request to backend (replace with actual endpoint and method)
  fetch('/api/addAsset', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(assetData),
  })
  .then(response => response.json())
  .then(data => {
    // Example: Handle success response (replace with actual success handling)
    console.log('Success:', data);
    alert('Asset added successfully!');
    // Example: Clear form fields (implement as needed)
    document.getElementById('assetId').value = '';
    document.getElementById('assetType').value = '';
    document.getElementById('status').value = '';
    document.getElementById('location').value = '';
  })
  .catch((error) => {
    // Example: Handle error (replace with actual error handling)
    console.error('Error:', error);
    alert('Error adding asset. Please try again.');
  });
}
