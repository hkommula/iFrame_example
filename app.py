import streamlit as st

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Webpage with iFrame</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        header {
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            text-align: center;
            padding: 40px 0;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        header h1 {
            font-size: 2.5em;
            margin: 0;
            letter-spacing: 1px;
        }
        iframe {
            width: 100%;
            height: 600px;
            border: 5px solid #4CAF50;
            border-radius: 10px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2);
        }
        main {
            padding: 20px;
            text-align: center;
        }
        main p {
            font-size: 1.2em;
            color: #333;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Our Modern Webpage</h1>
    </header>
    
    <main>
        <p>Here is some random text before the iframe component.</p>
        
        <!-- iFrame component pointing to Pano2VR index.html or any desired content -->
        <iframe src="output/index.html"></iframe>
        
        <p>Here is some random text after the iframe component.</p>
    </main>
</body>
</html>
"""

# Streamlit app
st.markdown(html_content, unsafe_allow_html=True)
