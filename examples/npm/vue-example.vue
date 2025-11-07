<!-- Vue Example - Using KardoCSS with Vue 3 -->
<!-- Install: npm install kardocss -->

<!-- 1. Import CSS in your main.js -->
<!-- import 'kardocss/dist/kardocss.min.css'; -->

<!-- 2. Use KardoCSS classes in your components -->
<template>
  <div :class="{ 'dark': darkMode }">
    <div class="k-min-h-screen k-bg-gray-100 dark:k-bg-gray-900">
      <!-- Header -->
      <header class="k-bg-primary k-text-white k-py-8">
        <div class="k-container k-text-center">
          <h1 class="k-text-4xl k-font-bold k-mb-2">
            KardoCSS + Vue
          </h1>
          <p class="k-text-xl">
            Modern CSS Framework for Vue
          </p>
        </div>
      </header>

      <!-- Dark Mode Toggle -->
      <div class="k-container k-py-6">
        <button
          @click="toggleDarkMode"
          class="k-bg-blue-500 hover:k-bg-blue-600 k-text-white k-px-6 k-py-3 k-rounded-lg k-transition-all k-duration-300"
        >
          {{ darkMode ? '☀️ Light Mode' : '🌙 Dark Mode' }}
        </button>
      </div>

      <!-- Content -->
      <main class="k-container k-py-12">
        <div class="k-grid k-grid-cols-1 md:k-grid-cols-3 k-gap-6">
          <Card
            v-for="feature in features"
            :key="feature.title"
            :title="feature.title"
            :description="feature.description"
            :icon="feature.icon"
          />
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const darkMode = ref(false);

const features = [
  {
    title: 'Responsive',
    description: 'Mobile-first design with breakpoints',
    icon: '📱'
  },
  {
    title: 'Dark Mode',
    description: 'Built-in dark mode support',
    icon: '🌓'
  },
  {
    title: 'Lightweight',
    description: 'Only 99KB minified, ~8KB with PurgeCSS',
    icon: '⚡'
  }
];

const toggleDarkMode = () => {
  darkMode.value = !darkMode.value;
  document.documentElement.classList.toggle('dark');
};
</script>

<!-- Card Component (can be in separate file) -->
<script setup>
defineProps({
  title: String,
  description: String,
  icon: String
});
</script>

<template>
  <div class="k-bg-white dark:k-bg-gray-800 k-p-6 k-rounded-lg k-shadow-md hover:k-shadow-lg k-transition-shadow k-duration-300">
    <div class="k-text-4xl k-mb-4">{{ icon }}</div>
    <h3 class="k-text-xl k-font-semibold k-mb-2 k-text-gray-900 dark:k-text-white">
      {{ title }}
    </h3>
    <p class="k-text-gray-600 dark:k-text-gray-300">
      {{ description }}
    </p>
  </div>
</template>

