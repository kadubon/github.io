const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  try {
    // Increase navigation timeout and use 'domcontentloaded' which is often faster
    await page.goto('https://orcid.org/0009-0004-4273-3365', { waitUntil: 'domcontentloaded', timeout: 30000 });

    // Wait for the container of the works list, which is more stable.
    await page.waitForSelector('#works-container', { timeout: 30000 });

    // A brief extra wait can sometimes help with tricky dynamic content
    await page.waitForTimeout(2000);

    const works = await page.$$eval('#works-container cy-list-item', (nodes) => {
      return nodes.map(node => {
        const titleElement = node.querySelector('cy-list-item-title a');
        const doiElement = node.querySelector('a[href*="doi.org"]');
        
        const title = titleElement ? titleElement.innerText.trim() : null;
        // Extract DOI from the href attribute
        const doi = doiElement ? doiElement.href.replace('https://doi.org/', '') : null;

        return { title, doi };
      }).filter(work => work.title && work.doi);
    });

    if (works.length === 0) {
        console.error('No works with DOIs were found. The page structure might have changed.');
        // For debugging, let's see the HTML content if no works are found
        // console.log(await page.content());
    } else {
        console.log(JSON.stringify(works, null, 2));
    }

  } catch (error) {
    console.error('Error scraping ORCID page:', error);
  } finally {
    await browser.close();
  }
})();