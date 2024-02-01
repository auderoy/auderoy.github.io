function fetchData(fileName) {
    fetch(fileName)
        .then(response => response.text())
        .then(data => {
            const [header, ...rows] = data.split('\n');
            const properties = header.split(',');
            rows.reverse();
            const spineImgContainer = document.querySelector('.spine-img-container');
            const imageUrls = [];
            rows.forEach(row => {
                const values = row.split(',');
                const title = values[properties.indexOf('Title')].trim();
                const length = parseFloat(values[properties.indexOf('Length')]);
                const pages = parseFloat(values[properties.indexOf('Pages')]);
                const color = values[properties.indexOf('Color')].trim();
                const imagePath = `spines/${title.replace(/[ ,.!?:/]+/g, '').toLowerCase()}.jpg`;
                imageUrls.push({ path: imagePath, title, length, pages, color });
            });
            loadImagesSequentially(imageUrls, spineImgContainer);
        })
        .catch(error => console.error('Error reading CSV file:', error));
}

function loadImagesSequentially(imageUrls, container) {
    let index = 0;
    function loadNextImage() {
        if (index < imageUrls.length) {
            const imageInfo = imageUrls[index];
            const image = new Image();
            image.src = imageInfo.path;
            image.className = 'spine-img';
            image.onload = () => {
                image.style.width = `${imageInfo.length * 30}px`; /*Lx30 or Lx22*/
                container.appendChild(image);
                index++;
                loadNextImage();
            };
            image.onerror = () => {
                /* console.error(`Error loading image: ${image.src}`); */
                const box = document.createElement('div');
                box.textContent = imageInfo.title;
                box.className = 'box';
                box.style.width = `${imageInfo.length * 30}px`; /*Lx30 or Lx20*/
                box.style.height = `${imageInfo.pages / 10}px`; /*L/10 or L/15*/
                box.style.backgroundColor = imageInfo.color;
                container.appendChild(box);
                index++;
                loadNextImage();
            };
        }
    }
    loadNextImage();
}