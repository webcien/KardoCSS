// Vite Example - Using KardoCSS with Vite
// Install: npm install kardocss

// main.js or main.ts
import 'kardocss/dist/kardocss.min.css';
import './style.css'; // Your custom styles

// Your app code here
document.querySelector('#app').innerHTML = `
  <div class="k-min-h-screen k-bg-gray-100 dark:k-bg-gray-900">
    <header class="k-bg-primary k-text-white k-py-8">
      <div class="k-container k-text-center">
        <h1 class="k-text-4xl k-font-bold k-mb-2">
          KardoCSS + Vite
        </h1>
        <p class="k-text-xl">
          Lightning-fast development with Vite
        </p>
      </div>
    </header>

    <main class="k-container k-py-12">
      <div class="k-grid k-grid-cols-1 md:k-grid-cols-3 k-gap-6">
        <div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md">
          <div class="k-text-4xl k-mb-4">⚡</div>
          <h3 class="k-text-xl k-font-semibold k-mb-2">Fast</h3>
          <p class="k-text-gray-600">Instant HMR with Vite</p>
        </div>
        
        <div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md">
          <div class="k-text-4xl k-mb-4">🎨</div>
          <h3 class="k-text-xl k-font-semibold k-mb-2">Beautiful</h3>
          <p class="k-text-gray-600">Utility-first CSS framework</p>
        </div>
        
        <div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md">
          <div class="k-text-4xl k-mb-4">📦</div>
          <h3 class="k-text-xl k-font-semibold k-mb-2">Lightweight</h3>
          <p class="k-text-gray-600">Only 99KB minified</p>
        </div>
      </div>
    </main>
  </div>
`;

// Optional: Dark mode toggle
const darkModeToggle = document.createElement('button');
darkModeToggle.className = 'k-fixed k-top-4 k-right-4 k-bg-blue-500 k-text-white k-px-4 k-py-2 k-rounded-lg';
darkModeToggle.textContent = '🌙 Toggle Dark Mode';
darkModeToggle.onclick = () => {
  document.documentElement.classList.toggle('dark');
};
document.body.appendChild(darkModeToggle);

