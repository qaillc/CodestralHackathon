import streamlit as st
import streamlit.components.v1 as components

# HTML content (your provided HTML goes here)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        #goalSpace { border: 1px solid #ccc; }
        .goal { cursor: pointer; }
        #info { margin-top: 20px; font-weight: bold; }
        #selectedGoal { margin-top: 10px; padding: 10px; border: 1px solid #ccc; background-color: #f0f0f0; }
        #hoverInfo { 
            position: absolute; 
            padding: 10px; 
            background-color: rgba(255, 255, 255, 0.9); 
            border: 1px solid #ccc; 
            border-radius: 5px; 
            font-size: 14px;
            max-width: 300px;
            display: none;
        }
    </style>
</head>
<body>

    <div id="goalSpace"></div>
    <div id="info"></div>
    <div id="selectedGoal"></div>
    <div id="hoverInfo"></div>

    <script>
        const width = 1200;
        const height = 800;
        const goals = [
            { id: 1, x: 100, y: 400, name: "Automate Data Import", description: "Develop scripts to automate exam data extraction from various sources (CSV, Excel, databases) using Pandas read_* functions." },
            { id: 2, x: 200, y: 300, name: "Data Cleaning", description: "Implement robust data cleaning processes to handle missing values, outliers, and inconsistencies in exam data using Pandas methods like dropna(), fillna(), and apply()." },
            { id: 3, x: 300, y: 200, name: "Data Transformation", description: "Utilize Pandas for complex data transformations such as pivoting exam results, melting question-wise scores, and creating derived features for analysis." },
            { id: 4, x: 400, y: 300, name: "Statistical Analysis", description: "Develop functions to automate statistical analysis of exam results, including descriptive statistics, hypothesis testing, and correlation analysis using Pandas and SciPy." },
            { id: 5, x: 500, y: 400, name: "Performance Metrics", description: "Create custom functions to calculate industry-standard exam performance metrics like item difficulty, discrimination index, and reliability coefficients using Pandas operations." },
            { id: 6, x: 200, y: 500, name: "Data Filtering", description: "Implement advanced filtering techniques to segment exam data based on various criteria (e.g., demographic info, score ranges) using boolean indexing and query() method in Pandas." },
            { id: 7, x: 300, y: 600, name: "Reporting Automation", description: "Develop automated reporting systems that use Pandas groupby() and agg() functions to generate summary statistics and performance reports for different exam cohorts." },
            { id: 8, x: 400, y: 500, name: "Data Visualization", description: "Create interactive dashboards for exam data visualization using Pandas with Plotly or Bokeh, allowing stakeholders to explore results dynamically." },
            { id: 9, x: 500, y: 600, name: "Time Series Analysis", description: "Implement time series analysis techniques using Pandas datetime functionality to track and forecast exam performance trends over multiple test administrations." },
            { id: 10, x: 300, y: 400, name: "Data Integration", description: "Develop processes to merge exam data with other relevant datasets (e.g., student information systems, learning management systems) using Pandas merge() and join() operations." },
            { id: 11, x: 600, y: 300, name: "Performance Optimization", description: "Improve the efficiency of Pandas operations on large exam datasets by utilizing techniques like chunking, multiprocessing, and query optimization." },
            { id: 12, x: 700, y: 400, name: "Machine Learning Integration", description: "Integrate machine learning models with Pandas for predictive analytics, such as predicting exam success or identifying at-risk students based on historical data." },
            { id: 13, x: 800, y: 500, name: "Custom Indexing", description: "Implement custom indexing strategies in Pandas to efficiently handle hierarchical exam data structures and improve data access patterns." },
            { id: 14, x: 900, y: 400, name: "Data Anonymization", description: "Develop Pandas-based workflows to anonymize sensitive exam data, ensuring compliance with privacy regulations while maintaining data utility for analysis." },
            { id: 15, x: 1000, y: 300, name: "Exam Item Analysis", description: "Create specialized functions using Pandas to perform detailed item analysis, including distractor analysis and reliability calculations for individual exam questions." },
            { id: 16, x: 600, y: 500, name: "Longitudinal Analysis", description: "Implement Pandas-based methods for tracking student performance across multiple exams over time, identifying learning trends and progress patterns." },
            { id: 17, x: 700, y: 600, name: "Adaptive Testing Analysis", description: "Develop analysis pipelines using Pandas to evaluate and optimize adaptive testing algorithms, including item selection strategies and scoring methods." },
            { id: 18, x: 800, y: 700, name: "Exam Equating", description: "Create Pandas workflows to perform exam equating, ensuring comparability of scores across different versions or administrations of an exam." },
            { id: 19, x: 900, y: 600, name: "Response Time Analysis", description: "Utilize Pandas to analyze exam response times, identifying patterns that may indicate guessing, test-taking strategies, or item difficulty." },
            { id: 20, x: 1000, y: 500, name: "Collaborative Filtering", description: "Implement collaborative filtering techniques using Pandas to recommend study materials or practice questions based on exam performance patterns." },
            { id: 21, x: 400, y: 700, name: "Exam Fraud Detection", description: "Develop anomaly detection algorithms using Pandas to identify potential exam fraud or unusual response patterns in large-scale testing programs." },
            { id: 22, x: 500, y: 800, name: "Standard Setting", description: "Create Pandas-based tools to assist in standard setting processes, analyzing expert judgments and examinee data to establish performance standards." },
            { id: 23, x: 600, y: 700, name: "Automated Reporting", description: "Implement automated report generation using Pandas and libraries like Jinja2 to create customized, data-driven exam reports for various stakeholders." },
            { id: 24, x: 700, y: 800, name: "Cross-validation", description: "Develop cross-validation frameworks using Pandas to assess the reliability and generalizability of predictive models in educational assessment contexts." },
            { id: 25, x: 800, y: 300, name: "API Integration", description: "Create Pandas-based interfaces to integrate exam data analysis workflows with external APIs, facilitating real-time data exchange and reporting." },
            { id: 26, x: 900, y: 200, name: "Natural Language Processing", description: "Implement NLP techniques using Pandas and libraries like NLTK to analyze free-text responses in exams, enabling automated scoring and content analysis." },
            { id: 27, x: 1000, y: 100, name: "Exam Blueprint Analysis", description: "Develop Pandas workflows to analyze exam blueprints, ensuring content coverage and alignment with learning objectives across multiple test forms." },
            { id: 28, x: 100, y: 600, name: "Differential Item Functioning", description: "Implement statistical methods using Pandas to detect and analyze differential item functioning (DIF) in exams, ensuring fairness across different demographic groups." },
            { id: 29, x: 200, y: 700, name: "Automated Feedback Generation", description: "Create Pandas-based systems to generate personalized feedback for test-takers based on their exam performance and identified areas for improvement." },
            { id: 30, x: 300, y: 800, name: "Exam Security Analysis", description: "Develop analytical tools using Pandas to assess and enhance exam security, including analysis of item exposure rates and detection of potential security breaches." }
        ];
        const connections = [
            { source: 1, target: 2 },
            { source: 2, target: 3 },
            { source: 3, target: 4 },
            { source: 4, target: 5 },
            { source: 5, target: 7 },
            { source: 6, target: 7 },
            { source: 7, target: 8 },
            { source: 8, target: 9 },
            { source: 9, target: 16 },
            { source: 10, target: 13 },
            { source: 11, target: 12 },
            { source: 12, target: 20 },
            { source: 13, target: 16 },
            { source: 14, target: 21 },
            { source: 15, target: 17 },
            { source: 16, target: 18 },
            { source: 17, target: 19 },
            { source: 18, target: 22 },
            { source: 19, target: 21 },
            { source: 20, target: 29 },
            { source: 21, target: 30 },
            { source: 22, target: 23 },
            { source: 23, target: 25 },
            { source: 24, target: 12 },
            { source: 25, target: 23 },
            { source: 26, target: 15 },
            { source: 27, target: 15 },
            { source: 28, target: 22 },
            { source: 29, target: 23 },
            { source: 30, target: 21 },
            // Additional connections for more interconnectivity
            { source: 1, target: 10 },
            { source: 2, target: 6 },
            { source: 3, target: 13 },
            { source: 4, target: 15 },
            { source: 5, target: 28 },
            { source: 8, target: 23 },
            { source: 11, target: 25 },
            { source: 14, target: 30 },
            { source: 24, target: 17 },
            { source: 26, target: 29 }
        ];
        const svg = d3.select("#goalSpace")
            .append("svg")
            .attr("width", width)
            .attr("height", height);
        const links = svg.selectAll("line")
            .data(connections)
            .enter()
            .append("line")
            .attr("x1", d => goals.find(g => g.id === d.source).x)
            .attr("y1", d => goals.find(g => g.id === d.source).y)
            .attr("x2", d => goals.find(g => g.id === d.target).x)
            .attr("y2", d => goals.find(g => g.id === d.target).y)
            .attr("stroke", "#999")
            .attr("stroke-width", 1)
            .attr("stroke-opacity", 0.6);
        const goalNodes = svg.selectAll("circle")
            .data(goals)
            .enter()
            .append("circle")
            .attr("cx", d => d.x)
            .attr("cy", d => d.y)
            .attr("r", 10)
            .attr("fill", d => {
                if (d.id <= 10) return "blue";
                if (d.id <= 20) return "green";
                return "orange";
            })
            .attr("class", "goal");
        const goalLabels = svg.selectAll("text")
            .data(goals)
            .enter()
            .append("text")
            .attr("x", d => d.x + 15)
            .attr("y", d => d.y)
            .text(d => d.name)
            .attr("font-size", "12px");
        const hoverInfo = d3.select("#hoverInfo");
        goalNodes.on("mouseover", function(event, d) {
            d3.select(this).attr("r", 15);
            hoverInfo.style("display", "block")
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 10) + "px")
                .html(`<strong>${d.name}</strong><br>${d.description}`);
        }).on("mouseout", function() {
            d3.select(this).attr("r", 10);
            hoverInfo.style("display", "none");
        });
        goalNodes.on("click", function(event, d) {
            updateSelectedGoalInfo(d);
        });
        function updateSelectedGoalInfo(goal) {
            const selectedGoalDiv = d3.select("#selectedGoal");
            selectedGoalDiv.html(`
                <h3>${goal.name}</h3>
                <p>${goal.description}</p>
            `);
        }
        svg.on("mousemove", function(event) {
            const [x, y] = d3.pointer(event);
            const closest = findClosestGoal(x, y);
            highlightClosestGoal(closest);
        });
        function findClosestGoal(x, y) {
            return goals.reduce((closest, goal) => {
                const distance = Math.sqrt(Math.pow(goal.x - x, 2) + Math.pow(goal.y - y, 2));
                return distance < closest.distance ? { goal, distance } : closest;
            }, { goal: null, distance: Infinity }).goal;
        }
        function highlightClosestGoal(goal) {
            d3.select("#info").html(`Closest goal: ${goal.name}`);
        }
    </script>
</body>
</html>
"""

# Streamlit app
def main():
    st.set_page_config(page_title="Exam Data Analysis Goals", layout="wide")
    
    st.title("Comprehensive Exam Data Analysis")
    st.write("This visualization shows 30 industry goals with connections for exam data analysis.")
    
    # Render the HTML content
    components.html(html_content, height=900, scrolling=True)
    
    st.write("Hover over the nodes to see more information about each goal.")
    st.write("Click on a node to see its details in the visualization.")

if __name__ == "__main__":
    main()