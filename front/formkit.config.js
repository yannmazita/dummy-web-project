import { fr } from '@formkit/i18n'
import { generateClasses } from '@formkit/themes'
import { genesisIcons } from '@formkit/icons'
import formkitTheme from './tailwind-formkit-theme.js'

export default {
    icons: {
        ...genesisIcons,
    },
    config: {
        classes: generateClasses(formkitTheme),
    },
    locales: { fr },
    locale: 'fr'
}
