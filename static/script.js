// ... (existing code)

function predict() {
    const xInput = document.getElementById('x-input').value;
    const data = new URLSearchParams();
    data.append('x', xInput);

    fetch('/predict', {
        method: 'POST',
        body: data,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.prediction.toFixed(2);
        // Set the x value in the plot form and submit the form
        document.getElementById('plot-x-input').value = xInput;
        document.getElementById('plot-form').submit();
    })
    .catch(error => console.error('Error:', error));
}


function showPlot() {
    const xInput = document.getElementById('x-input').value;
    const plotURL = `/plot?x=${xInput}`;

    // Open the plot in a new tab
    window.open(plotURL, '_blank');
}


// ... (existing code)


// function predict() {
//     const xInput = document.getElementById('x-input').value;
//     const data = new URLSearchParams();
//     data.append('x', xInput);

//     fetch('/predict', {
//         method: 'POST',
//         body: data,
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('result').innerText = data.prediction.toFixed(2);
//     })
//     .catch(error => console.error('Error:', error));
// }

// function plot() {
//     const xInput = document.getElementById('x-input').value;

//     fetch(`/plot?x=${xInput}`)
//         .then(response => response.text())
//         .then(plotBase64 => {
//             const img = new Image();
//             img.src = `data:image/png;base64,${plotBase64}`;

//             const modal = document.createElement('div');
//             modal.className = 'modal';
//             modal.innerHTML = `
//                 <span class="close" onclick="this.parentNode.remove()">&times;</span>
//                 <img src="${img.src}" alt="Plot">
//             `;

//             document.body.appendChild(modal);
//         })
//         .catch(error => console.error('Error:', error));
// }



// function predict() {
//     const xInput = document.getElementById('x-input').value;
//     const data = { x: xInput };

//     fetch('/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data),
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('result').innerText = data.prediction.toFixed(2);
//     })
//     .catch(error => console.error('Error:', error));
// }

// function plot() {
//     const xInput = document.getElementById('x-input').value;
    
//     fetch(`/plot?x=${xInput}`)
//         .then(response => response.text())
//         .then(plotBase64 => {
//             const img = new Image();
//             img.src = `data:image/png;base64,${plotBase64}`;

//             const modal = document.createElement('div');
//             modal.className = 'modal';
//             modal.innerHTML = `
//                 <span class="close" onclick="this.parentNode.remove()">&times;</span>
//                 <img src="${img.src}" alt="Plot">
//             `;

//             document.body.appendChild(modal);
//         })
//         .catch(error => console.error('Error:', error));
// }




// // function predict() {
// //     const xValue = document.getElementById('x-input').value;
// //     fetch(`/predict?x=${xValue}`)
// //         .then(response => response.json())
// //         .then(data => {
// //             document.getElementById('result').innerText = data.prediction;
// //         })
// //         .catch(error => console.error('Error:', error));
// // }
