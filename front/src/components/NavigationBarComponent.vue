<template>
<div class="navbar bg-base-100">
  <div class="navbar-start">
    <div class="dropdown">
      <label tabindex="0" class="btn btn-ghost lg:hidden">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
      </label>
      <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
          <li><router-link to="/">Accueil</router-link></li>
          <li><router-link to="/agenda">Agenda</router-link></li>
          <li><router-link to="/inscription">Comment s'inscrire</router-link></li>
          <li><router-link to="/contactez-nous">Contactez-nous</router-link></li>
          <li><router-link to="/boutique">Boutique</router-link></li>
        <li>
            <router-link to="/espace-club">Accès espace club</router-link>
          <ul class="p-2">
            <li><a>Gestion des salles</a></li>
            <li><a>Gestion des arbitres</a></li>
            <li><a>Gestion des adhérents</a></li>
            <li><a>Espace formation</a></li>
          </ul>
        </li>
      </ul>
    </div>
    <a class="btn btn-ghost text-xl">SCP Volley</a>
  </div>

  <div class="navbar-center hidden lg:flex">
    <ul class="menu menu-horizontal px-1">
          <li tabindex="0"><router-link to="/">Accueil</router-link></li>
          <li><router-link to="/agenda">Agenda</router-link></li>
          <li><router-link to="/inscription">Comment s'inscrire</router-link></li>
          <li><router-link to="/contactez-nous">Contactez-nous</router-link></li>
          <li><router-link to="/boutique">Boutique</router-link></li>
      <li>
        <details>
          <summary>Espace club</summary>
          <ul class="p-2">
              <li tabindex="0"><router-link to="/espace-club">Accès espace club</router-link></li>
            <li><a>Gestion des salles</a></li>
            <li><a>Gestion des arbitres</a></li>
            <li><a>Gestion des adhérents</a></li>
            <li><a>Espace formation</a></li>
          </ul>
        </details>
      </li>
    </ul>
  </div>
  <div class="navbar-end">
  </div>
</div>
</template>
