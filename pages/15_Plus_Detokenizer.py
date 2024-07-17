import streamlit as st
import streamlit.components.v1 as components
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set page configuration
st.set_page_config(page_title="First Conscious Quadrant with Detokenizer", layout="wide")

# Title
st.title("First Conscious Quadrant with Detokenizer")

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
            window.parent.postMessage({type: 'clickedCoordinate', value: combinedCoord.toString().padStart(10, '0')}, '*');
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

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained('gpt2')



# Detokenization section
st.header("Detokenization")
token_ids = st.text_input("Enter token IDs (concatenated without spaces):", "")

def split_token_ids(concatenated_ids, length=5):
    return [concatenated_ids[i:i+length] for i in range(0, len(concatenated_ids), length)]

def remove_leading_zeros(grouped_ids):
    return [id.lstrip('0') for id in grouped_ids]

if st.button("Detokenize"):
    split_ids = split_token_ids(token_ids)
    cleaned_ids = remove_leading_zeros(split_ids)
    cleaned_token_ids_str = ' '.join(cleaned_ids)
    token_id_list = [int(id) for id in cleaned_ids if id.isdigit()]
    detokenized_sentence = tokenizer.decode(token_id_list)
    st.write("Grouped and cleaned token IDs:")
    st.write(cleaned_token_ids_str)
    st.write("Detokenized sentence:")
    st.write(detokenized_sentence)


# Load the model
gpt2 = AutoModelForCausalLM.from_pretrained('gpt2')

# Display help for the GPT-2 model
if st.checkbox("Show GPT-2 Model Help"):
    st.write("Help GPT2")
    st.help(gpt2)

# JavaScript to handle messages from the iframe
components.html(
    """
    <script>
    window.addEventListener('message', function(event) {
        if (event.data.type === 'clickedCoordinate') {
            document.querySelector('input[aria-label="Enter token IDs (concatenated without spaces):"]').value = event.data.value;
            document.querySelector('button[kind="secondary"]').click();
        }
    }, false);
    </script>
    """
)