const configs = document.querySelectorAll('.config-btn');

configs.forEach(config => config.addEventListener('click', () => configClicked(config)));

const configClicked = (config) => {
    const contents = document.querySelectorAll('.content');

    contents.forEach(content => content.classList.remove('show'));

    const contentId = config.getAttribute('content-id');
    const content = document.getElementById(contentId);
    
    content.classList.add('show');
}