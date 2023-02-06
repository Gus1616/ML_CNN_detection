<template>
    <nav>
        <h3>{{ title }}</h3>

      <ul>
        <li v-for="item in items" :key="item.text">
          <a :href="item.link">{{ item.text }}</a>
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'MenuBar',

    data() {
      return {
        title: 'The Skin Dectection App ',

        items: [
          { text: 'Home', link: '/' },
          { text: 'About', link: '/about' },
          { text: 'Contact', link: '/contact' }
        ]
      }
    }
  }
  </script>
  
  <style>
  nav h3 {
    margin: 0;
    padding: 0 30px;
  }
   nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: left;
    align-items: center;
    height: 60px;
    background-color: #333;
    color: #fff;
  }
    
  
    nav ul {
      list-style: none;
      display: flex;
      margin: 0;
      padding: 0;
    }
  
    nav li {
      display: flex;
      padding: 0 10px;
    }
  
    nav a {
      color: #fff;
      text-decoration: none;
    }
  </style>
  