---
layout: default
title: Recipes
permalink: /recipes/
---

# Recipes

<ul>
  {% for page in site.pages %}
    {% if page.path contains "recipes/" and page.title %}
      <li>
        <a href="{{ page.url }}">{{ page.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>
