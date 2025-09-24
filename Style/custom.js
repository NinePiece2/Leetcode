// LeetCode Solutions - Custom JavaScript Enhancements

document.addEventListener('DOMContentLoaded', function() {
    
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add copy to clipboard functionality for code blocks
    function addCopyButtons() {
        const codeBlocks = document.querySelectorAll('pre code');
        codeBlocks.forEach(block => {
            const pre = block.parentElement;
            if (!pre.querySelector('.copy-button')) {
                const copyButton = document.createElement('button');
                copyButton.className = 'copy-button';
                copyButton.innerHTML = '📋';
                copyButton.title = 'Copy to clipboard';
                copyButton.style.cssText = `
                    position: absolute;
                    top: 8px;
                    right: 8px;
                    background: rgba(255, 255, 255, 0.1);
                    border: none;
                    border-radius: 4px;
                    padding: 4px 8px;
                    cursor: pointer;
                    font-size: 12px;
                    opacity: 0.7;
                    transition: opacity 0.2s ease;
                `;
                
                copyButton.addEventListener('click', async () => {
                    try {
                        await navigator.clipboard.writeText(block.textContent);
                        copyButton.innerHTML = '✅';
                        copyButton.style.color = '#4caf50';
                        setTimeout(() => {
                            copyButton.innerHTML = '📋';
                            copyButton.style.color = '';
                        }, 2000);
                    } catch (err) {
                        console.error('Failed to copy text: ', err);
                        copyButton.innerHTML = '❌';
                        setTimeout(() => {
                            copyButton.innerHTML = '📋';
                        }, 2000);
                    }
                });

                copyButton.addEventListener('mouseenter', () => {
                    copyButton.style.opacity = '1';
                });

                copyButton.addEventListener('mouseleave', () => {
                    copyButton.style.opacity = '0.7';
                });

                pre.style.position = 'relative';
                pre.appendChild(copyButton);
            }
        });
    }

    // Add difficulty badges to problem titles
    function addDifficultyBadges() {
        const problemTitles = document.querySelectorAll('h1, h2');
        problemTitles.forEach(title => {
            const text = title.textContent.toLowerCase();
            let badgeClass = '';
            let badgeText = '';

            // Check for difficulty indicators in the title
            if (text.includes('easy') || text.includes('simple')) {
                badgeClass = 'difficulty-easy';
                badgeText = 'Easy';
            } else if (text.includes('medium') || text.includes('moderate')) {
                badgeClass = 'difficulty-medium';
                badgeText = 'Medium';
            } else if (text.includes('hard') || text.includes('difficult')) {
                badgeClass = 'difficulty-hard';
                badgeText = 'Hard';
            }

            if (badgeClass && !title.querySelector('.difficulty-badge')) {
                const badge = document.createElement('span');
                badge.className = `difficulty-badge ${badgeClass}`;
                badge.textContent = badgeText;
                badge.style.marginLeft = '10px';
                title.appendChild(badge);
            }
        });
    }

    // Add reading time estimation
    function addReadingTime() {
        const content = document.querySelector('.md-content__inner');
        if (content && !document.querySelector('.reading-time')) {
            const text = content.textContent || content.innerText || '';
            const wordsPerMinute = 200;
            const wordCount = text.trim().split(/\s+/).length;
            const readingTime = Math.ceil(wordCount / wordsPerMinute);
            
            if (readingTime > 0) {
                const readingTimeElement = document.createElement('div');
                readingTimeElement.className = 'reading-time';
                readingTimeElement.innerHTML = `
                    <span style="
                        display: inline-block;
                        background: var(--md-default-fg-color--lightest);
                        color: var(--md-default-fg-color);
                        padding: 4px 8px;
                        border-radius: 12px;
                        font-size: 0.7rem;
                        margin-bottom: 1rem;
                        opacity: 0.8;
                    ">
                        📖 ${readingTime} min read
                    </span>
                `;
                
                const firstHeading = content.querySelector('h1');
                if (firstHeading) {
                    firstHeading.insertAdjacentElement('afterend', readingTimeElement);
                }
            }
        }
    }

    // Add table of contents for long pages
    function addTableOfContents() {
        const headings = document.querySelectorAll('.md-content h2, .md-content h3');
        if (headings.length > 3 && !document.querySelector('.custom-toc')) {
            const toc = document.createElement('div');
            toc.className = 'custom-toc';
            toc.innerHTML = '<h4>📚 Contents</h4>';
            
            const list = document.createElement('ul');
            list.style.cssText = `
                list-style: none;
                padding: 0;
                margin: 0;
                background: var(--md-default-bg-color--light);
                border-radius: 8px;
                padding: 1rem;
                margin-bottom: 2rem;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            `;

            headings.forEach((heading, index) => {
                const id = heading.id || `heading-${index}`;
                if (!heading.id) heading.id = id;
                
                const listItem = document.createElement('li');
                listItem.style.marginBottom = '0.5rem';
                
                const link = document.createElement('a');
                link.href = `#${id}`;
                link.textContent = heading.textContent;
                link.style.cssText = `
                    text-decoration: none;
                    color: var(--md-default-fg-color);
                    font-size: 0.8rem;
                    padding-left: ${heading.tagName === 'H3' ? '1rem' : '0'};
                    display: block;
                    border-radius: 4px;
                    padding: 0.25rem 0.5rem;
                    transition: all 0.2s ease;
                `;
                
                link.addEventListener('mouseenter', () => {
                    link.style.background = 'var(--md-accent-fg-color--transparent)';
                });
                
                link.addEventListener('mouseleave', () => {
                    link.style.background = 'transparent';
                });
                
                listItem.appendChild(link);
                list.appendChild(listItem);
            });
            
            toc.appendChild(list);
            
            const firstHeading = document.querySelector('.md-content h1');
            if (firstHeading) {
                firstHeading.insertAdjacentElement('afterend', toc);
            }
        }
    }

    // Initialize all enhancements
    addCopyButtons();
    addDifficultyBadges();
    addReadingTime();
    addTableOfContents();

    // Re-run enhancements on dynamic content changes
    const observer = new MutationObserver((mutations) => {
        let shouldUpdate = false;
        mutations.forEach((mutation) => {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                shouldUpdate = true;
            }
        });
        if (shouldUpdate) {
            setTimeout(() => {
                addCopyButtons();
                addDifficultyBadges();
                addReadingTime();
                addTableOfContents();
            }, 100);
        }
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + K for search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const searchInput = document.querySelector('.md-search__input');
            if (searchInput) {
                searchInput.focus();
            }
        }
        
        // Escape to close search
        if (e.key === 'Escape') {
            const searchForm = document.querySelector('.md-search__form');
            if (searchForm && searchForm.classList.contains('md-search__form--active')) {
                document.querySelector('.md-search__input').blur();
            }
        }
    });

    // Add scroll progress indicator
    function addScrollProgress() {
        if (!document.querySelector('.scroll-progress')) {
            const progressBar = document.createElement('div');
            progressBar.className = 'scroll-progress';
            progressBar.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 0%;
                height: 3px;
                background: linear-gradient(90deg, var(--md-primary-fg-color), var(--md-accent-fg-color));
                z-index: 1000;
                transition: width 0.1s ease;
            `;
            document.body.appendChild(progressBar);

            window.addEventListener('scroll', () => {
                const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
                progressBar.style.width = Math.min(scrolled, 100) + '%';
            });
        }
    }

    addScrollProgress();

    console.log('🚀 LeetCode Solutions site enhancements loaded!');
});