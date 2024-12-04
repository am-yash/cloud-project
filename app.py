from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Project Landing Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f9fc;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 50px;
            background-color: #ffffff;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        header .logo {
            font-size: 24px;
            font-weight: bold;
            color: #3c5a9a;
        }

        header nav a {
            margin: 0 15px;
            text-decoration: none;
            color: #3c5a9a;
            font-size: 16px;
        }

        header nav a:hover {
            text-decoration: underline;
        }

        .hero {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 50px;
            background-color: #e9f4ff;
        }

        .hero .text {
            max-width: 50%;
        }

        .hero h1 {
            font-size: 48px;
            color: #333;
        }

        .hero h1 span {
            color: #3c5a9a;
        }

        .hero p {
            font-size: 18px;
            color: #555;
            margin: 20px 0;
        }

        .hero .buttons a {
            display: inline-block;
            margin: 10px 10px 0 0;
            padding: 15px 30px;
            text-decoration: none;
            font-size: 16px;
            color: #fff;
            background-color: #3c5a9a;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        .hero .buttons a:hover {
            background-color: #2d4373;
        }

        .hero .image img {
            max-width: 100%;
        }

        footer {
            text-align: center;
            padding: 20px;
            background-color: #ffffff;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        footer p {
            color: #555;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">CodeWithCloud</div>
        <nav>
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
        </nav>
    </header>

    <section class="hero">
        <div class="text">
            <h1>Welcome to <span>CloudWorld</span><br> I'm <span>Cloud Developer</span></h1>
            <p>Build scalable, secure, and modern cloud solutions with our expertise. Join us to explore limitless possibilities in the cloud.</p>
            <div class="buttons">
                <a href="#">Explore Projects</a>
                <a href="#">Documentation</a>
            </div>
        </div>
        <div class="image">
            <img src="https://via.placeholder.com/500x300" alt="Cloud Illustration">
        </div>
    </section>

    <footer>
        <p>&copy; 2024 CloudWorld. All rights reserved.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
