document.addEventListener('DOMContentLoaded', function() {
    const orcidId = '0009-0004-4273-3365';
    const apiUrl = `https://pub.orcid.org/v3.0/${orcidId}/works`;
    const publicationsList = document.getElementById('publications-list');

    fetch(apiUrl, { 
        headers: { 'Accept': 'application/json' } 
    })
    .then(response => response.json())
    .then(data => {
        const works = data.group;
        if (works && works.length > 0) {
            // Sort works by last modified date in descending order
            works.sort((a, b) => {
                const dateA = a['last-modified-date'] ? new Date(a['last-modified-date'].value) : new Date(0);
                const dateB = b['last-modified-date'] ? new Date(b['last-modified-date'].value) : new Date(0);
                return dateB - dateA; // Newest first
            });

            let html = '<ul>';
            works.forEach(work => {
                const summary = work['work-summary'][0];
                const title = summary.title.title.value;
                const pubYear = summary['publication-date'] ? summary['publication-date'].year.value : 'N/A';
                
                // Format the last modified date
                const lastModified = new Date(work['last-modified-date'].value);
                const lastModifiedString = lastModified.toLocaleDateString('en-CA'); // YYYY-MM-DD format

                let doi = '';
                if (summary['external-ids'] && summary['external-ids']['external-id']) {
                    const doiObject = summary['external-ids']['external-id'].find(id => id['external-id-type'] === 'doi');
                    if (doiObject) {
                        doi = doiObject['external-id-value'];
                    }
                }

                html += `
                    <li>
                        <span class="title">${title}</span>
                        <span class="year">Published: ${pubYear}</span>
                        <span class="last-modified">Last Modified: ${lastModifiedString}</span>
                        ${doi ? `<a href="https://doi.org/${doi}" target="_blank" class="doi-link">View Publication (DOI)</a>` : ''}
                    </li>
                `;
            });
            html += '</ul>';
            publicationsList.innerHTML = html;
        } else {
            publicationsList.innerHTML = '<p>No publications found.</p>';
        }
    })
    .catch(error => {
        console.error('Error fetching publications:', error);
        publicationsList.innerHTML = '<p>Could not load publications. Please try again later.</p>';
    });
});