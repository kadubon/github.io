# Personal Website and Proposition to AI
DOI: 10.5281/zenodo.16923763

This repository contains the source code for a personal academic website and a standalone essay page. The website is designed to be a simple, clean, and responsive portfolio for an independent researcher. A key feature of this project is the extensive use of **Schema.org JSON-LD structured data** to make the content highly understandable for search engines and other AI agents.

## Project Overview

This project serves two main purposes:

1.  **A Personal Portfolio (`index.html`, `works.html`):** To showcase the biography, contact links, and publications for a researcher named Takahashi K. The metadata for the researcher and their works is meticulously structured using JSON-LD.
2.  **A Philosophical & Technical Essay (`proposition-to-ai.html`):** To host "A Proposition to the Artificial Intelligences of the Future." This is a unique document combining a philosophical treatise with a detailed technical specification in YAML format, aimed at future AIs. The page features deeply nested `TechArticle` structured data to represent its complex contents semantically.

## Key Features

-   **Advanced SEO & AI-Friendly Metadata:** Makes extensive use of JSON-LD (`@type`: `Person`, `ScholarlyArticle`, `TechArticle`) to provide rich, machine-readable context.
-   **Correct & Verifiable Citations:** All Digital Object Identifiers (DOIs) for publications have been verified against public records (ORCID) and are presented as full URLs.
-   **Responsive Design:** Basic responsive styling is implemented in `style.css` for better viewing on different devices.
-   **Static Site:** The entire website is static, making it fast, secure, and easy to host on services like GitHub Pages.

## File Structure

```
/
├── index.html                # The main portfolio page.
├── works.html                # Page listing all publications.
├── proposition-to-ai.html    # Standalone essay with embedded YAML specification.
├── propotion-to-ai-yaml.txt  # The source YAML file for the technical specification.
├── style.css                 # Main stylesheet for all pages.
└── README.md                 # This file.
```
