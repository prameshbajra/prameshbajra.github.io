# Pramesh Bajracharya.

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badge/)

# Personal website
<https://prameshbajra.com>

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

## Writing a post

Create `_posts/YYYY-MM-DD-slug.md`. The published URL is `/blog/<slug>/` — the
date in the filename does not appear in it.

```yaml
---
layout: post
title: "How a thing works"
date: 2026-08-07
description: "One sentence, under ~155 characters. This is the Google snippet."
tags: [networking, homelab]      # slugs from _data/topics.yml, most specific first
image: /static/assets/img/og/slug.png
---
```

- **`description`** is required in practice — it becomes the meta description and
  the blurb on `/blog/`. Don't just restate the title; that wastes the snippet.
- **`tags`** must be slugs that exist in `_data/topics.yml`. The first one decides
  the coloured pill and which `/topics/<slug>/` hub shows the related-posts block.
  Adding a topic means adding it to both `_data/topics.yml` and `topics/`.
- **`last_modified_at: 2026-08-07`** — add when you materially revise a post. It
  feeds `dateModified` in the article schema, `<lastmod>` in the sitemap, and the
  feed entry, which is how search engines see the post as refreshed. Without it,
  `dateModified` just mirrors the publish date.
- **`redirect_from`** — only needed if a post's slug changes, to keep the old URL alive.

Then generate the social card and shrink any screenshots:

```bash
python3 build/generate-og-images.py
python3 build/optimize-post-images.py
```

Both are idempotent and need Pillow. The optimizer resizes to roughly 2x rendered
size and never writes a file that came out larger than the original, so re-running
it is safe. Write images as `<img src="…" alt="…" width="…" height="…"
loading="lazy" decoding="async">` — the intrinsic `width`/`height` reserve layout
space, and any display sizing belongs in `style="width: …"`, not the attributes.

### Verify before publishing
Run Jekyll's build and doctor checks to ensure templates render cleanly and config issues are caught:

```bash
bundle exec jekyll doctor
bundle exec jekyll build
```

The build output appears in `_site/`. Commit only source files—leave `_site/` untracked when pushing to GitHub.
