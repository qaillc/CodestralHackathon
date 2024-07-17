import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="First Conscious Quadrant", layout="wide")

# Title
st.title("First Conscious Quadrant")

# HTML content (your original HTML/JS code)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Base 50256 Grid</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .container {
            text-align: center;
        }
        #grid {
            max-width: 80vmin;
            max-height: 80vmin;
            border: 1px solid #ccc;
        }
        .output {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <canvas id="grid" width="1000" height="1000"></canvas>
        <div id="clickedOutput" class="output">Click on the grid to select a coordinate</div>
        <div id="hoverOutput">Hover Coordinate: (X: 0, Y: 0)</div>
    </div>
    <script>
        const canvas = document.getElementById('grid');
        const ctx = canvas.getContext('2d');
        const clickedOutput = document.getElementById('clickedOutput');
        const hoverOutput = document.getElementById('hoverOutput');

        const gridSizeX = 50255;
        const gridSizeY = 50255;
        const cellSizeX = canvas.width / 16;
        const cellSizeY = canvas.height / 16;

        function drawGrid() {
            ctx.fillStyle = 'white';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.strokeStyle = '#ccc';
            ctx.lineWidth = 1;

            for (let i = cellSizeX; i < canvas.width; i += cellSizeX) {
                ctx.beginPath();
                ctx.moveTo(i, 0);
                ctx.lineTo(i, canvas.height);
                ctx.stroke();
            }

            for (let i = cellSizeY; i < canvas.height; i += cellSizeY) {
                ctx.beginPath();
                ctx.moveTo(0, i);
                ctx.lineTo(canvas.width, i);
                ctx.stroke();
            }

            ctx.fillStyle = 'black';
            ctx.font = '16px Arial';
            ctx.fillText('0,0', 5, canvas.height - 5);
            ctx.fillText(`${gridSizeX},0`, canvas.width - 60, canvas.height - 5);
            ctx.fillText(`0,${gridSizeY}`, 5, 20);
            ctx.fillText(`${gridSizeX},${gridSizeY}`, canvas.width - 100, 20);
        }

        function getCoordinates(event) {
            const rect = canvas.getBoundingClientRect();
            const x = Math.min(Math.floor((event.clientX - rect.left) / rect.width * gridSizeX), gridSizeX);
            const y = Math.min(gridSizeY - Math.floor((event.clientY - rect.top) / rect.height * gridSizeY), gridSizeY);
            return { x, y };
        }

        canvas.addEventListener('mousemove', (event) => {
            const { x, y } = getCoordinates(event);
            hoverOutput.textContent = `Hover Coordinate: (X: ${x}, Y: ${y})`;
        });

        canvas.addEventListener('click', (event) => {
            const { x, y } = getCoordinates(event);
            const combinedCoord = x * 100000 + y;
            clickedOutput.textContent = `Clicked Coordinate: ${combinedCoord.toString().padStart(10, '0')}`;
        });

        canvas.addEventListener('mouseleave', () => {
            hoverOutput.textContent = 'Hover Coordinate: (X: 0, Y: 0)';
        });

        drawGrid();
    </script>
</body>
</html>
"""

# Embed the HTML content
components.html(html_content, height=700, scrolling=True)

# Additional Streamlit content (optional)
st.write("The interactive grid above is embedded from HTML/JavaScript.")
st.write("You can click on the grid to select a coordinate, and hover to see the current position.")