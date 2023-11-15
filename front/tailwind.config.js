/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');

const extendColors = {
    // Custom hexadecimal colors
    secondary: '#9949E',
    warning: '#f9c018',
};

export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
        "./tailwind-formkit-theme.js",
    ],
    theme: {
        extend: {
            colors: extendColors,
            fontFamily: {
                sans: ['Montserrat', ...defaultTheme.fontFamily.sans],
            },
        },
        daisyui: {
            themes: [
                "light",
                "dark",
                "cupcake",
                "bumblebee",
                "emerald",
                "corporate",
                "synthwave",
                "retro",
                "cyberpunk",
                "valentine",
                "halloween",
                "garden",
                "forest",
                "aqua",
                "lofi",
                "pastel",
                "fantasy",
                "wireframe",
                "black",
                "luxury",
                "dracula",
                "cmyk",
                "autumn",
                "business",
                "acid",
                "lemonade",
                "night",
                "coffee",
                "winter",
                "dim",
                "nord",
                "sunset",
            ],
        },
    },
    plugins: [
        require('daisyui'),
        require('@tailwindcss/typography'),
        //require('@formkit/themes/tailwindcss'),
    ],
}

