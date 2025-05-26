/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.{html,js}"],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '968px',
      xl: '1440px',

    },
    extend: {
      fontFamily: {
        sans: ['Work Sans', 'sans-serif'],
      },
      colors: {
        primary: {
          DEFAULT: '#6366F1', // indigo-500 ---buttons, accents
          dark: '#4F46E5',    // indigo-600 ---hover states
          light: '#E0E7FF',   // indigo-100 ---background highlights
        },
        secondary: '#14B8A6',     // teal-500 ---tags, secondary cta's
        background: '#F9FAFB',    // gray-50 ---app background
        card: '#FFFFFF',                  // ---task containers, modals
        border: '#E5E7EB',        // gray-200 ---task containers, modals
        text: {
          primary: '#111827',     // gray-900 ---main text
          secondary: '#6B7280',   // gray-500 ---descriptions, metadata
        },
        danger: '#EF4444',        // red-500 ---delete actions, errors
        success: '#10B981',       // green-500 ---completed tasks
      },
    },
  },
  plugins: [],
}

