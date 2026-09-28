// Universal Real-time Autocomplete Search Engine for tzshouce.cyou
document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('searchInput');
  const searchForm = document.getElementById('searchForm');
  const searchContainer = document.querySelector('.header-search');

  if (!searchInput || !searchForm || !searchContainer) return;

  // Create dropdown container
  const dropdown = document.createElement('div');
  dropdown.className = 'search-dropdown-panel';
  searchContainer.appendChild(dropdown);

  let searchIndex = [];
  let isFetching = false;
  let selectedIndex = -1;

  // Friendly Chinese category badge map
  function getSectionBadge(section) {
    const map = {
      'jichang-tuijian': '精选机场',
      'jiaocheng': '新手教程',
      'jishu': '协议与进阶',
      'wenti': '避坑与 FAQ',
      'providers': '28家测评',
      'service': '服务专区'
    };
    return map[section] || '文章';
  }

  // Hot Search Tags for fast filtering
  const hotTags = ['灵动云', '暮光网络', '飞猫云', 'Clash教程', '小火箭订阅', 'Timeout超时', '4K秒开', 'IPLC专线', '优惠码', '防走丢'];

  // Load index.json lazily on focus or type
  function loadIndex(callback) {
    if (searchIndex.length > 0) {
      if (callback) callback();
      return;
    }
    if (isFetching) return;
    isFetching = true;

    fetch('/index.json')
      .then(res => res.json())
      .then(data => {
        searchIndex = data || [];
        isFetching = false;
        if (callback) callback();
      })
      .catch(err => {
        console.error('Failed to load search index:', err);
        isFetching = false;
      });
  }

  function highlightQuery(text, query) {
    if (!query) return text;
    const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`(${escaped})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
  }

  function renderDropdown(query) {
    const q = query.trim().toLowerCase();
    dropdown.innerHTML = '';

    if (!q) {
      // Render Hot Tags when empty
      let html = `<div class="search-dropdown-header">🔥 热门关联词搜索</div><div class="search-dropdown-tags"><div class="search-tags-list">`;
      hotTags.forEach(tag => {
        html += `<span class="search-tag-chip" data-tag="${tag}">${tag}</span>`;
      });
      html += `</div></div>`;
      dropdown.innerHTML = html;
      dropdown.classList.add('active');
      bindTagClick();
      return;
    }

    // Perform Keyword Matching across Title, Summary, Keywords, Section
    const results = searchIndex.filter(item => {
      const titleMatch = item.title && item.title.toLowerCase().includes(q);
      const summaryMatch = item.summary && item.summary.toLowerCase().includes(q);
      const sectionMatch = item.section && item.section.toLowerCase().includes(q);
      return titleMatch || summaryMatch || sectionMatch;
    }).slice(0, 8); // Top 8 live dynamic results

    if (results.length === 0) {
      dropdown.innerHTML = `
        <div class="search-dropdown-header">未找到与 "${q}" 完全匹配的结果</div>
        <div class="search-dropdown-tags">
          <div class="search-tags-title">试一试点击以下高频关键词：</div>
          <div class="search-tags-list">
            ${hotTags.map(tag => `<span class="search-tag-chip" data-tag="${tag}">${tag}</span>`).join('')}
          </div>
        </div>
      `;
      dropdown.classList.add('active');
      bindTagClick();
      return;
    }

    let html = `<div class="search-dropdown-header">已为你关联到 ${results.length} 篇相关文章</div>`;
    results.forEach((item, idx) => {
      const badge = getSectionBadge(item.section);
      const titleHighlighted = highlightQuery(item.title, query);
      html += `
        <a href="${item.permalink}" class="search-dropdown-item ${idx === selectedIndex ? 'selected' : ''}">
          <div class="search-item-title">${titleHighlighted}</div>
          <div class="search-item-meta">
            <span class="search-item-badge">${badge}</span>
            <span>查看完整内容 →</span>
          </div>
        </a>
      `;
    });

    dropdown.innerHTML = html;
    dropdown.classList.add('active');
  }

  function bindTagClick() {
    const chips = dropdown.querySelectorAll('.search-tag-chip');
    chips.forEach(chip => {
      chip.addEventListener('click', function () {
        const tag = this.getAttribute('data-tag');
        searchInput.value = tag;
        renderDropdown(tag);
        searchInput.focus();
      });
    });
  }

  // Event Listeners
  searchInput.addEventListener('focus', function () {
    loadIndex(() => {
      renderDropdown(searchInput.value);
    });
  });

  searchInput.addEventListener('input', function () {
    selectedIndex = -1;
    loadIndex(() => {
      renderDropdown(this.value);
    });
  });

  // Form Submission (Redirects to wenti or current page with query)
  searchForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const q = searchInput.value.trim();
    if (q) {
      window.location.href = '/wenti/?q=' + encodeURIComponent(q);
    }
  });

  // Click Outside to Close Dropdown
  document.addEventListener('click', function (e) {
    if (!searchContainer.contains(e.target)) {
      dropdown.classList.remove('active');
    }
  });

  // Handle URL Query String Filtering on List Pages (e.g. /wenti/?q=灵动云)
  const urlParams = new URLSearchParams(window.location.search);
  const qParam = urlParams.get('q');
  if (qParam) {
    const qLower = qParam.trim().toLowerCase();
    searchInput.value = qParam;

    const cards = document.querySelectorAll('.list-article-card');
    const container = document.querySelector('.article-layout');

    if (cards.length > 0 && container) {
      let matchCount = 0;
      cards.forEach(card => {
        const titleText = card.querySelector('.list-card-title')?.textContent.toLowerCase() || '';
        const summaryText = card.querySelector('.list-card-summary')?.textContent.toLowerCase() || '';
        if (titleText.includes(qLower) || summaryText.includes(qLower)) {
          card.style.display = 'flex';
          matchCount++;
        } else {
          card.style.display = 'none';
        }
      });

      const banner = document.createElement('div');
      banner.style.cssText = 'background:#eff6ff; border:1px solid #dbeafe; border-radius:6px; padding:0.75rem 1rem; margin-bottom:1.25rem; font-size:0.9rem; color:#1e40af; width:100%;';
      banner.innerHTML = `🔍 关联词搜索结果: <strong>"${qParam}"</strong>，共找到 <strong>${matchCount}</strong> 篇相关文章。<a href="${window.location.pathname}" style="float:right; color:#2563eb; font-weight:700; text-decoration:underline;">清空搜索 ✕</a>`;
      container.parentNode.insertBefore(banner, container);
    }
  }
});
