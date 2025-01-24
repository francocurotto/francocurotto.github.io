---
layout: default
title: Recipes
---

<h1>{{ page.title }}</h1>

<ul>
  {% for post in site.recipes %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
