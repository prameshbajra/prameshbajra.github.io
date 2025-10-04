# Pramesh Bajracharya.

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badge/)

# Personal website
<http://prameshbajra.github.io>

My learnings and prototypes that I would like to share.

## Local Development

### Prerequisites
- Ruby (use the version installed locally or via rbenv/rvm) with Bundler available
- Node.js 16+ (asset watcher and build scripts)

### Install dependencies
Run these once per environment:

```bash
gem install bundler # skip if Bundler is already available
bundle install
npm install
```

By default Bundler installs gems into the global path. To keep them vendored, run `bundle config set --local path 'vendor/bundle'` before `bundle install`.

### Start the site locally
Launch Jekyll in watch mode with livereload:

```bash
bundle exec jekyll serve --livereload
```

This serves the site at `http://127.0.0.1:4000`. Keep the command running while you edit Markdown posts, layouts, or data files; changes trigger automatic rebuilds and browser refreshes. If you tweak Sass or JavaScript bundles, start the theme's helper in another terminal:

```bash
npm run dev
```

### Verify before publishing
Run Jekyll's build and doctor checks to ensure templates render cleanly and config issues are caught:

```bash
bundle exec jekyll doctor
bundle exec jekyll build
```

The build output appears in `_site/`. Commit only source files—leave `_site/` untracked when pushing to GitHub.
