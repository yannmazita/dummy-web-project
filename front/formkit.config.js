import { fr } from '@formkit/i18n'
import { genesisIcons } from '@formkit/icons'
import { createMultiStepPlugin } from '@formkit/addons'
import '@formkit/addons/css/multistep'

const config = {
    icons: {
        genesisIcons,
    },
    plugins: [createMultiStepPlugin()],
    locales: { fr },
    locale: 'fr',
}

export default config
