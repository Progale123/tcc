const configs = document.querySelectorAll('.config-btn');

configs.forEach(config => config.addEventListener('click', () => configClicked(config)));

const configClicked = (config) => {
    configs.forEach(config => config.classList.remove('active'));
    config.classList.add('active');
    const contents = document.querySelectorAll('.content');
    contents.forEach(content => content.classList.remove('show'));

    const contentId = config.getAttribute('content-id');
    const content = document.getElementById(contentId);
    
    content.classList.add('show');
}

const currentActiveconfig = document.querySelector('.config-btn');
configClicked(currentActiveconfig);