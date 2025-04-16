
# Blog Website Flask

This project is a simple blog website built using Flask. It showcases the backend functionality with templates and static files to create a fully functional web application.

## Features

- A clean project structure with modular components.
- HTML templates for the frontend (`home.html`, `post.html`, `create.html`, `base.html`).
- Integrated SQLite database (`posts.db`) for storing blog post data.
- Custom styling using a CSS file (`style.css`).

## Project Structure

```plaintext
Blog_Website_Flask/
│
├── app.py             # Main application logic
├── templates/         # HTML templates
│   ├── home.html      # Homepage
│   ├── post.html      # Individual post page
│   ├── create.html    # Page to create a new post
│   └── base.html      # Common layout for all pages
├── static/            # Static files like CSS
│   └── style.css      # Custom CSS styles
├── posts.db           # SQLite database
└── README.md          # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.x
- Flask (install using pip)
- SQLite (comes pre-installed with Python)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Anchal7905/Blog_Website_Flask.git
   cd Blog_Website_Flask
   ```

2. Install the required Python packages:

   ```bash
   pip install flask
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Access the application at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## License

This project is released under the MIT License. Feel free to use and modify it for your own purposes.

## Acknowledgments

- Flask Documentation
- Bootstrap CSS for inspiration
- GitHub for hosting this project

---
