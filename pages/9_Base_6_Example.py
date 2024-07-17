import streamlit as st
import streamlit.components.v1 as components

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2D Canvas Base 6 with Hidden State in Red</title>
    <style>
        body { font-family: Arial, sans-serif; }
        #coordinate-display { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background-color: rgba(255, 255, 255, 0.7);
            padding: 5px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    
    <div style="position: relative;">
        <canvas id="graphCanvas" width="500" height="400" style="border: 1px solid #000;"></canvas>
        <div id="coordinate-display"></div>
    </div>

    <script>
        const canvas = document.getElementById('graphCanvas');
        const ctx = canvas.getContext('2d');
        const coordinateDisplay = document.getElementById('coordinate-display');

        function shouldHighlightCoordinate(num) {
            return ['6', '7', '8', '9'].some(digit => num.toString().includes(digit));
        }

        function drawGraph() {
            // Clear canvas
            ctx.fillStyle = '#f0f0f0';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw grid
            ctx.strokeStyle = '#999';
            ctx.lineWidth = 0.5;
            for (let i = 0; i <= 55; i += 5) {
                let x = i / 55 * canvas.width;
                let y = canvas.height - (i / 55 * canvas.height);
                
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, canvas.height);
                ctx.stroke();

                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(canvas.width, y);
                ctx.stroke();

                // Draw labels
                ctx.fillStyle = 'black';
                ctx.font = '12px Arial';
                ctx.fillText(i.toString(), x, canvas.height - 5);
                ctx.fillText(i.toString(), 5, y);
            }

            // Draw highlighted areas
            ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
            for (let i = 0; i <= 55; i++) {
                if (shouldHighlightCoordinate(i)) {
                    ctx.fillRect(i / 55 * canvas.width, 0, canvas.width / 55, canvas.height);
                    ctx.fillRect(0, canvas.height - ((i + 1) / 55 * canvas.height), canvas.width, canvas.height / 55);
                }
            }
        }

        function updateCoordinateDisplay(event) {
            const rect = canvas.getBoundingClientRect();
            const x = Math.min(55, Math.round((event.clientX - rect.left) / canvas.width * 55));
            const y = Math.round((1 - (event.clientY - rect.top) / canvas.height) * 55);
            const combined = x * 100 + y;
            
            coordinateDisplay.textContent = `Coordinate: ${combined}`;
            coordinateDisplay.style.color = shouldHighlightCoordinate(combined) ? 'red' : 'black';
        }

        canvas.addEventListener('mousemove', updateCoordinateDisplay);

        drawGraph();
    </script>
</body>
</html>
"""

# Streamlit app
def main():
    st.set_page_config(page_title="Interactive 2D Graph", layout="wide")
    
    st.title("2D Interactive Graph Base 6")
    st.write("With Hidden State in Red")
    
    # Embed the HTML content
    components.html(html_content, height=600)

if __name__ == "__main__":
    main()