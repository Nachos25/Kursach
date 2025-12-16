/** @type {import('tailwindcss').Config} */
export default {
  darkMode: "class",
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#f3f6ff",
          100: "#e6edff",
          500: "#7c9cff",
          600: "#5c7fff",
          700: "#3e63ff"
        }
      }
    }
  },
  plugins: []
};




