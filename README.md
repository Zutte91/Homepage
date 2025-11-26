# IT Consulting & Services Website

A professional website built with Flask (Python) and Tailwind CSS for IT consulting, training, trading, network, homelab, and software development services.

## Features

- **Home Page**: Overview of services and contact information
- **About Page**: Personal and professional information
- **Projects Hub**: Interactive page to showcase current projects
- **Services Pages**: Detailed pages for each service offering:
  - IT Consulting
  - Training
  - Trading
  - Network
  - Homelab
  - Software Development
- **Navigation**: Header with dropdown menu for services
- **Footer**: Links to all pages and sections

## Design

- Color scheme: White and Blue
- Responsive design using Tailwind CSS
- Modern, clean interface

## Setup Instructions

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

3. **Access the website:**
   Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
Homepage/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    ├── base.html         # Base template with header and footer
    ├── index.html        # Home page
    ├── about.html        # About me page
    ├── projects.html     # Projects hub
    ├── services.html     # Services overview
    └── services/
        ├── it_consulting.html
        ├── training.html
        ├── trading.html
        ├── network.html
        ├── homelab.html
        └── software_development.html
```

## Customization

- Edit contact information in `templates/index.html`
- Update personal information in `templates/about.html`
- Add projects in `templates/projects.html` (JavaScript section)
- Modify service descriptions in individual service pages
- Customize colors in `templates/base.html` (Tailwind config)

## Development

The application runs in debug mode by default. For production, set `debug=False` in `app.py`.


