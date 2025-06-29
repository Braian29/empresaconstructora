// tailwind.config.js (o dentro del <script> en base.html si usas el CDN JIT)
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Open Sans"', 'sans-serif'],
        oswald: ['"Oswald"', 'sans-serif'],
      },
      colors: {
        // La paleta principal basada en el rojo vibrante FB3535
        primary: {
          50: '#FEE5E5',  // Un rojo muy pálido, más vibrante que EED4D4
          100: '#FDDCDC',
          200: '#F8B5B5',
          300: '#F38E8E',
          400: '#EE6767',
          500: '#FB3535', // ¡Tu rojo principal!
          600: '#DB2E2E',
          700: '#BB2727',
          800: '#9B2020',
          900: '#7B1A1A',
          950: '#5C1414',
        },
        // Colores específicos de tu paleta que no forman una escala completa
        'brand-dark': '#0E0E0E', // Para texto o fondos muy oscuros
        'brand-gray': '#9E9E9E', // Para texto o bordes grises
        'brand-light-pink': '#EED4D4', // Para fondos sutiles o acentos claros
        'brand-muted-red': '#CA4C4C', // Para un rojo más discreto o secundario
        'brand-light-blue-gray': '#CCD4D4', // Para fondos o elementos neutros con un toque azulado

        // Mantener colores accent existentes (WhatsApp) si aplican
        accent: {
          'whatsapp': '#25D366',
          'whatsapp-dark': '#1DA851',
        },
        // Puedes mantener la escala de grises predeterminada de Tailwind si la necesitas para otros propósitos
        // Si no la necesitas, puedes borrar esta línea para eliminarla de tu CSS final (con un build process)
        gray: require('tailwindcss/colors').gray, 
      },
    },
  },
  plugins: [],
}