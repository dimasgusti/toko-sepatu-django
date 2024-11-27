/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',  
    './components/**/*.{html,js}',  
    './static/**/*.{html,js}',     
    './**/*.html',                 
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};