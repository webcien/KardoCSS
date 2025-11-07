// React Example - Using KardoCSS with React
// Install: npm install kardocss

// 1. Import CSS in your main file (e.g., index.js or App.js)
import 'kardocss/dist/kardocss.min.css';

// 2. Use KardoCSS classes in your components
import React, { useState } from 'react';

function App() {
  const [darkMode, setDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    document.documentElement.classList.toggle('dark');
  };

  return (
    <div className={darkMode ? 'dark' : ''}>
      <div className="k-min-h-screen k-bg-gray-100 dark:k-bg-gray-900">
        {/* Header */}
        <header className="k-bg-primary k-text-white k-py-8">
          <div className="k-container k-text-center">
            <h1 className="k-text-4xl k-font-bold k-mb-2">
              KardoCSS + React
            </h1>
            <p className="k-text-xl">
              Modern CSS Framework for React
            </p>
          </div>
        </header>

        {/* Dark Mode Toggle */}
        <div className="k-container k-py-6">
          <button
            onClick={toggleDarkMode}
            className="k-bg-blue-500 hover:k-bg-blue-600 k-text-white k-px-6 k-py-3 k-rounded-lg k-transition-all k-duration-300"
          >
            {darkMode ? '☀️ Light Mode' : '🌙 Dark Mode'}
          </button>
        </div>

        {/* Content */}
        <main className="k-container k-py-12">
          <div className="k-grid k-grid-cols-1 md:k-grid-cols-3 k-gap-6">
            <Card
              title="Responsive"
              description="Mobile-first design with breakpoints"
              icon="📱"
            />
            <Card
              title="Dark Mode"
              description="Built-in dark mode support"
              icon="🌓"
            />
            <Card
              title="Lightweight"
              description="Only 99KB minified, ~8KB with PurgeCSS"
              icon="⚡"
            />
          </div>
        </main>
      </div>
    </div>
  );
}

function Card({ title, description, icon }) {
  return (
    <div className="k-bg-white dark:k-bg-gray-800 k-p-6 k-rounded-lg k-shadow-md hover:k-shadow-lg k-transition-shadow k-duration-300">
      <div className="k-text-4xl k-mb-4">{icon}</div>
      <h3 className="k-text-xl k-font-semibold k-mb-2 k-text-gray-900 dark:k-text-white">
        {title}
      </h3>
      <p className="k-text-gray-600 dark:k-text-gray-300">
        {description}
      </p>
    </div>
  );
}

export default App;

