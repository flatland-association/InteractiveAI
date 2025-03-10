<img align="left" width="128" height="128" src="./public/android-chrome-512x512.png" alt="InteractiveAI logo" />

# ​ InteractiveAI Front

​ [![Node](https://img.shields.io/badge/Node-339933?style=plastic&logo=nodedotjs&logoColor=fff)](https://nodejs.org) [![Vue](https://img.shields.io/badge/Vue-35495E?style=plastic&logo=vuedotjs&logoColor=fff)](https://vuejs.org) [![Vite](https://img.shields.io/badge/Vite-%23646CFF.svg?style=plastic&logo=vite&logoColor=fff)](https://vitejs.dev) [![TypeScript](https://img.shields.io/badge/Typescript-%23007ACC.svg?style=plastic&logo=typescript&logoColor=fff)](https://www.typescriptlang.org) [![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=plastic&logo=Leaflet&logoColor=fff)](https://leafletjs.com) [![D3](https://img.shields.io/badge/D3-F9A03C?style=plastic&logo=d3.js&logoColor=fff)](https://d3js.org) [![Axios](https://img.shields.io/badge/Axios-671ddf?&style=plastic&logo=axios&logoColor=fff)](https://axios-http.com)

InteractiveAI platform provides support in augmented decision-making for complex steering systems.  
The platform make use of the project OperatorFabric for notification management and authentication.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#environment-variables">Environment variables</a></li>
    <li>
      <a href="#adding-your-custom-entity">Adding your custom entity</a>
      <ul>
        <li><a href="#structure">Structure</a></li>
        <li><a href="#config-file">Config file</a></li>
        <li><a href="#type-support-for-your-custom-entity">Type Support for your custom entity</a></li>
      </ul>
    </li>
    <li>
      <a href="#project-setup">Project Setup</a>
      <ul>
        <li><a href="#compile-and-hot-reload-for-development">Compile and Hot-Reload for Development</a></li>
        <li><a href="#type-check-compile-and-minify-for-production">Type-Check, Compile and Minify for Production</a></li>
        <li><a href="#run-unit-tests-with-vitest">Run Unit Tests with Vitest</a></li>
        <li><a href="#run-end-to-end-tests-with-cypress">Run End-to-End Tests with Cypress</a></li>
        <li><a href="#lint-with-eslint">Lint with ESLint</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#recommended-ide-setup">Recommended IDE Setup</a></li>
    <li><a href="#type-support-for-vue-imports-in-ts">Type Support for `.vue` Imports in TS</a></li>
    <li><a href="#customize-configuration">Customize configuration</a></li>
    <li><a href="#packages-used">Packages used</a></li>

  </ol>
</details>

## Environment variables

If you're using a different API location than the root location of the frontend, you can use env variables to set it:

- `VITE_API` for the default API
- `VITE_ENTITY_SIMU` for entity-specific API (`VITE_POWERGRID_SIMU` in the example).

In this case, you may need to disable CORS protection if the APIs are not configured properly.

```
chromium-browser --disable-web-security --user-data-dir="[some directory here]"
```

## Adding your custom entity

Adding your own entity (eg `ENTITY`) is done simply by adding your folder in `src/entities/ENTITY`.
Make sure its name matches exactly the entity created in OperatorFabric.

### Structure

```sh
src/entities/ENTITY
├── assets
│   ├── img                 # Custom assets
│   │   └── example.webp
│   ├── logo.svg            # Your logo in svg
│   └── theme.scss          # CSS variables to overwrite default theme
├── CAB                     # Define your own panels
│   ├── components          # Custom components
│   │   └── Example.vue
│   ├── Assistant.vue       # Your assistant
│   ├── Context.vue         # Your context
│   ├── Notifications.vue   # Your notifications
│   └── Timeline.vue        # Your timeline
├── locales                 # Custom locales
│   ├── en.json
│   └── fr.json
├── api.ts                  # Your custom api (optional)
└── types.ts                # Your custom types
```

### Config file

In `src/entities/config.ts`, add your new entity :

```ts
// Import your theme here
import './ENTITY/assets/theme.scss'

// Import your types here
// cf. Type Support for your custom entity
import type { ENTITY } from './ENTITY/types'

// Add your entity and config here
// hydrated: automatically fetch metadata for cards
// darkMode: use dark mode
export const ENTITIES_CONFIG = {
  ENTITY: { hydrated: true, darkMode: true }
}

// Bind your types here
type EntitiesTypes = {
  ENTITY: ENTITY
} as const
```

### Type Support for your custom entity

In `src/entities/ENTITY/types.ts`, you can define your custom types as follow:

```ts
export type ENTITY = {
  Context: any // Context returned by context service
  Metadata: any // Custom metadata added on cards
  Action: any // Actions returned by recommendation service
}
```

It is also the right place to define your other custom types.  
You can then import and add your types to `src/config.ts` (cf. [Adding your custom entity](#adding-your-custom-entity))

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
npm run dev: {mode} # run dev environment where {mode} is
                    # demo, development, prod, production, simu
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
npm run build: {mode} # build specific environment where {mode} is
                      # demo, development, prod, production, simu
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Run End-to-End Tests with [Cypress](https://www.cypress.io/)

```sh
npm run test:e2e:dev
```

This runs the end-to-end tests against the Vite development server.
It is much faster than the production build.

But it's still recommended to test the production build with `test:e2e` before deploying (e.g. in CI environments):

```sh
npm run build
npm run test:e2e
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Contributing

Commits use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/#summary) specification. You can easily compose your commit message using `npm run commit`.  
[Husky](https://typicode.github.io/husky/) automatically checks your commit message, format and lint your files, and checks the typing.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin) to make the TypeScript language service aware of `.vue` types.

If the standalone TypeScript plugin doesn't feel fast enough to you, Volar has also implemented a [Take Over Mode](https://github.com/johnsoncodehk/volar/discussions/471#discussioncomment-1361669) that is more performant. You can enable it by the following steps:

1. Disable the built-in TypeScript Extension
   1. Run `Extensions: Show Built-in Extensions` from VSCode's command palette
   2. Find `TypeScript and JavaScript Language Features`, right click and select `Disable (Workspace)`
2. Reload the VSCode window by running `Developer: Reload Window` from the command palette.

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Packages used

- **[Vue](https://vuejs.org/guide/introduction.html)**
- [Vue router](https://router.vuejs.org/guide/) for routing
- [Axios](https://axios-http.com/docs/intro) for networking
- [Pinia](https://pinia.vuejs.org/core-concepts/) for store
- [Mitt](https://github.com/developit/mitt) for event hub
- [D3](https://d3js.org/getting-started) for data visualisation
- [Leaflet](https://leafletjs.com/reference.html) for maps
- [Lucide](https://lucide.dev/icons/) for icons
- [date-fns](https://date-fns.org/docs/Getting-Started) for date formatting
- [Vue I18n](https://vue-i18n.intlify.dev/) for internationalization
