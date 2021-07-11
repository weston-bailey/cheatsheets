# TypeScript Resources

---

#### Reading/tutorials

* Docs are great: [TypeScript Docs / Handbook](https://www.typescriptlang.org/docs)
* Good resource put together by some benevolent dev: [TypeScript Deep Dive by @basarat](https://basarat.gitbooks.io/typescript/)
* [Adding Typscript to Create React App](https://create-react-app.dev/docs/adding-typescript/)
* Crashcoursey-style blog on [TypScript Type Notation](https://2ality.com/2018/04/type-notation-typescript.html)
* [Rules of Type Inference](https://www.typescriptlang.org/docs/handbook/type-inference.html)
* [Learn x in y minutes where x is TypeScript](https://learnxinyminutes.com/docs/typescript/)

#### Other Media:

* Podcast episode from Syntax.FM doing high-level chat on [why/where/how of Typescript](https://syntax.fm/show/324/typescript-fundamentals)
* YouTube Tutorial/overall walkthrough of Typescript that acts as a [long-form codelong/lecture](https://www.youtube.com/watch?v=BwuLxPH8IDs&t=1s)
* first minute of this video is a great explainer on the [WHY of Typescript](https://www.youtube.com/watch?v=bAB_nNf8-a0)

#### TypeScript Shell Commands Cheat Sheet

Handy table of TypeScript (and ts related) commands to keep in your back pocket:

| command | thing it does |
|---------|---------------|
| `npm install -g typescript` | installs TypeScript globall with npm |
| `tsc -v` | check your version of typescript |
| `tsc <fileName.ts>` | compiles `fileName.ts` to `fileName.js` |
| `tsc -w <fileName.ts>` | auto compiles `fileName.ts` to `fileName.js` on save (like nodemon) |
| `tsc --init` | creates a `tsconfig.json` |
| `tsc -p tsconfig.json` | compiles as a project using the config json, can be combined with the -w flag
| `npm --save-dev @types/<package name>` | save type declaration files for node packages: example `npm i --save-dev @types/express @types/dotenv @types/node`
| `create-react-app --template typescript <react-app-folder-name>` | creates a new react app in a folder called `<react-app-folder-name>` with typescript as the base of the project
| `npx express-generator-typescript "Backend"` | spins up and express backend template with typescript |

___

