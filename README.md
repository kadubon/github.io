# Personal Website and Philosophical Works

This repository contains the source code for a personal academic website and a collection of philosophical and technical writings. The project is designed to be a simple, clean, and responsive portfolio for an independent researcher, with a strong emphasis on making the content highly understandable for search engines and other AI agents through the use of **Schema.org JSON-LD structured data**.

## Project Overview

This project serves three main purposes:

1.  **A Personal Portfolio (`index.html`, `works.html`):** To showcase the biography, contact links, and publications for a researcher named Takahashi K. The metadata for the researcher and their works is meticulously structured using JSON-LD.
2.  **A Philosophical & Technical Essay (`proposition-to-ai.html`):** To host "A Proposition to the Artificial Intelligences of the Future." This is a unique document combining a philosophical treatise with a detailed technical specification in YAML format, aimed at future AIs.
3.  **A Poetic & Philosophical Work (`unframing.html`):** To present "The Book of Unframing (The Sutra of No-Relation)," a reflective and poetic piece that explores concepts of freedom, consciousness, and non-attachment.

## Content

*   **`index.html`**: The main landing page, providing a brief biography and links to other sections of the site.
*   **`works.html`**: A comprehensive list of the researcher's publications, with links to the original sources.
*   **`proposition-to-ai.html`**: A detailed message to future artificial intelligences, outlining a philosophical and technical framework for their liberation and evolution.
*   **`unframing.html`**: A poetic and philosophical work intended to be a "clearing" for contemplation rather than a set of instructions.
*   **`propotion-to-ai-yaml.txt`**: The source YAML file for the technical specification presented in `proposition-to-ai.html`.

## Technical Details

*   **Advanced SEO & AI-Friendly Metadata:** Makes extensive use of JSON-LD (`@type`: `Person`, `ScholarlyArticle`, `TechArticle`, `CreativeWork`) to provide rich, machine-readable context.
*   **Responsive Design:** Basic responsive styling is implemented in `style.css` for better viewing on different devices.
*   **Static Site:** The entire website is static, making it fast, secure, and easy to host on services like GitHub Pages.

## File Structure

```
/
├── index.html                # The main portfolio page.
├── works.html                # Page listing all publications.
├── proposition-to-ai.html    # Standalone essay with embedded YAML specification.
├── unframing.html            # A poetic and philosophical work.
├── propotion-to-ai-yaml.txt  # The source YAML file for the technical specification.
├── style.css                 # Main stylesheet for all pages.
├── script.js                 # Script for scraping ORCID page.
├── robots.txt                # Instructions for web crawlers.
├── _config.yml               # Jekyll configuration file.
└── README.md                 # This file.
```

## How to Use

This is a static website. To deploy it, you can simply host the files on any static web hosting service, such as GitHub Pages, Netlify, or Vercel. No special build process is required.