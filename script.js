// Fetch the data from the API
fetch('http://localhost:8000/news')
    .then(response => response.json())
    .then(data => {
        // Get the articles div
        const articlesDiv = document.querySelector('.articles');

        // Loop over each article in the data
        for (const article of data) {
            // Create a new div for the article group
            const articleGroup = document.createElement('div');
            articleGroup.className = 'article-group';

            // Create a new h2 for the article title
            const title = document.createElement('h2');
            title.className = 'article-title';
            const titleLink = document.createElement('a');
            titleLink.href = article.link;
            titleLink.textContent = article.title;
            title.appendChild(titleLink);

            // Create a new p for the article author
            if (article.author) {
                const author = document.createElement('p');
                author.className = 'article-author';
                author.textContent = `By ${article.author}`;
                articleGroup.appendChild(author);
            }

            // Create a new p for the article description
            const description = document.createElement('p');
            description.className = 'article-text';
            description.textContent = article.description;

            // Add the title, author, and description to the article group
            articleGroup.appendChild(title);
            articleGroup.appendChild(description);

            // Add the article group to the articles div
            articlesDiv.appendChild(articleGroup);
        }
    })
    .catch(error => console.error('Error:', error));